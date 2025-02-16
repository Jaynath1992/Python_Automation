masterip=${1}
echo "Master ip $masterip"
ver=$(echo "netapp1!" | sudo -S  kubelet --version | awk '{print $2}')
echo "Current version $ver"
res=$(echo $ver | while IFS=v read a b; do echo "$b"; done)
current_ver=$(echo $res | while IFS=. read a b c; do echo "$a.$b"; done)
echo "Current major version $current_ver"
major_nex_ver=`echo $current_ver + 0.01 | bc `
next_ver=$(apt-cache madison kubeadm | grep ${major_nex_ver} | head -n 1 |  awk '{print $3}')
echo "Next version $next_ver"
nodename=$(hostname)
echo "Hostname $nodename"

echo "netapp1!" | sudo -S  apt-mark unhold kubeadm && \
sudo apt-get update &&  sudo apt-get install -y kubeadm=$next_ver && \
sudo apt-mark hold kubeadm

echo "netapp1!" | sudo -S  kubeadm version
kubelet_ver=$(sudo kubelet --version | awk '{print $2}')
echo "netapp1!" | sudo -S kubeadm upgrade node config --kubelet-version=${kubelet_ver:1}

sshpass -p netapp1! ssh -o StrictHostKeyChecking=no root@$masterip "hostname; echo netapp1! | sudo -S kubectl drain $nodename --ignore-daemonsets --delete-local-data; exit"

echo "netapp1!" | sudo -S  apt-mark unhold kubelet kubectl && \
echo "netapp1!" | sudo -S  apt-get update && sudo apt-get install -y kubelet=$next_ver kubectl=$next_ver && \
echo "netapp1!" | sudo -S  apt-mark hold kubelet kubectl

echo "netapp1!" | sudo -S  systemctl daemon-reload
echo "netapp1!" | sudo -S  systemctl restart kubelet

# replace <cp-node-name> with the name of your control plane node
sshpass -p netapp1! ssh -o StrictHostKeyChecking=no root@$masterip "hostname; echo netapp1! | sudo -S kubectl uncordon $nodename; sleep 10; sudo kubectl get node -o wide; exit"
