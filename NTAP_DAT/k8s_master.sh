## this is k8s master.sh file for deploying packages on k8s master
#!/bin/bash -xe


echo "Ubuntu version installed"
lsb_release -d

echo "hostname"
hostname

echo "Memory Usage"
free

echo "CPU usage"
top -d 5 | head -n 15

echo "Uptime"
uptime

usage_exit() {
    echo "Unknown syntax; exiting."
    echo "master-k8s.sh --master-ip <ip-addr>"
    echo " or "
    echo "master-k8s.sh"
    exit
}

while [[ $# -gt 0 ]]; do
    curopt="$1"
    case $curopt in
        -m|--master-ip)
            if [[ -n "$2" ]]; then
                master_ip="$2"
                shift
                shift
	    else
                usage_exit
            fi
        ;;
        *)
	    usage_exit
        ;;
    esac
done

if [[ $(id -u) -ne 0 ]]; then
    echo "You are logged in as $(id -u -n). Please sudo su and become root to run this script."
    exit
fi

if [[ -z "$master_ip" ]]; then
    echo "Enter master node ip: "
    read master_ip
fi

echo "Master ip entered: ${master_ip}"
export NODE1_IP=$master_ip


echo "adding a swap entry in the /etc/fstab"
swapoff -a
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
echo "checking the contents of /etc/fstab"
echo "$(cat /etc/fstab)"
###
# Install our base kubernetes admin components
echo " updating, Installing HTTPS support components, curl"
apt-get update && apt-get install -y apt-transport-https curl
echo "Retrieve the key for the Kubernetes repo and add it to your key manager"
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
echo "Add the kubernetes repo to your system"
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update

k8sversion=1.21.14
kubelet=1.21.14-00
kubeadm=1.21.14-00
kubectl=1.21.14-00
kubernetes_cni=1.1.1-00

echo "installing kubelet:${kubelet}, kubeadm:${kubeadm}, kubectl:${kubectl} and kubernetes-cni:${kubernetes_cni} "
apt-get install -y kubelet=${kubelet} kubeadm=${kubeadm} kubectl=${kubectl} kubernetes-cni=${kubernetes_cni} --allow-change-held-packages

echo 'Creating directory /etc/systemd/system/kubelet.service.d'
mkdir -p /etc/systemd/system/kubelet.service.d

echo 'Creating /etc/systemd/system/kubelet.service.d/override.conf'
cat << EOF > /etc/systemd/system/kubelet.service.d/override.conf
[Service]
Environment="KUBELET_EXTRA_ARGS=--node-ip=${master_ip} --v=6"
EOF

echo 'Modifying /etc/systemd/system/kubelet.service.d/10-kubeadm.conf'
sed -e 's/KUBELET_EXTRA_ARGS$/KUBELET_EXTRA_ARGS --cgroup-driver=cgroupfs --pod-infra-container-image "gcr.io\/google_containers\/pause-amd64:3.1"/' -i  /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

sleep 10
echo "Restart the kubelet daemon"
systemctl daemon-reload

echo " removing the kubeadm log file"
rm -f /var/log/kubeadm.log
echo "Kubernetes master initialization"
kubeadm init --token-ttl 0 --pod-network-cidr=192.168.0.0/16 --apiserver-advertise-address=${master_ip} --kubernetes-version=v${k8sversion} --ignore-preflight-errors=all| tee /var/log/kubeadm.log

mkdir -p $HOME/.kube
echo "Create a copy of the Kubernetes admin.conf file in the .kube directory"
sudo /bin/cp -f /etc/kubernetes/admin.conf $HOME/.kube/config
echo "Change the ownership of the file to match your regular user profile"
sudo chown $(id -u):$(id -g) $HOME/.kube/config

echo "Install Calico CNI provider on your Kubernetes cluster"
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.24.5/manifests/calico.yaml

sleep 30
echo "Control plane node  isolation"
kubectl taint nodes --all node-role.kubernetes.io/master-

sleep 10
echo "Viewing nodes"
kubectl get nodes

echo "Get the info of the cluster"
kubectl cluster-info

echo "check if the master in ready state"
kubectl get nodes|grep master | awk '{print $2}'

echo "Set the NetApp managed mirrored repo"
file=/etc/docker/daemon.json
var="\"registry-mirrors\": [\"http://docker.repo.eng.netapp.com/\"]"

if [ ! -f ${file} ]; then
    echo "Not found ${file}"
    echo "Creating ${file}"
    touch ${file}
    sudo chmod 644 ${file}
fi

echo "Found ${file}"
if [ -z "$(cat ${file})" ]; then
    echo "${file} is empty"
    echo "Insert NetApp managed mirrored repo entry"
    echo -e "{\n}" >> ${file}
    sed -i -e "/^{/a ${var}" ${file}
elif grep -qs ${var} "${file}"; then
    echo "Netapp managed mirrored repo setting existed."
else
    echo "Insert NetApp managed mirrored repo entry"
    sed -i -e "/^{/a ${var}," ${file}
fi

echo "Restart the Docker Daemon"
systemctl restart docker
