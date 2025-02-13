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

if [[ $(id -u) -ne 0 ]]; then
    echo "You are logged in as $(id -u -n). Please sudo su and become root to run this script."
    exit
fi

echo "Enter worker node ip: "
read worker_ip

# Install our base kubernetes admin components
echo "updating, installing HTTPS support components,curl"
apt-get update && apt-get install -y apt-transport-https curl
echo "retrieve the key for kubernetes repo and add it to your key manager"
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
echo "add the kubernetes repo to your system"
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb http://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update

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
Environment="KUBELET_EXTRA_ARGS=--node-ip=${worker_ip}"
EOF

echo 'Modifying /etc/systemd/system/kubelet.service.d/10-kubeadm.conf'
sed -e 's/KUBELET_EXTRA_ARGS$/KUBELET_EXTRA_ARGS --cgroup-driver=cgroupfs --pod-infra-container-image "gcr.io\/google_containers\/pause-amd64:3.1"/' -i  /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

sleep 10

systemctl daemon-reload
swapoff -a

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
