echo "netapp1!" | sudo -S  apt update
ver=$(kubectl get node -o wide | grep master | awk '{print $5}')
echo "Current version $ver"
res=$(echo $ver | while IFS=v read a b; do echo "$b"; done)
current_ver=$(echo $res | while IFS=. read a b c; do echo "$a.$b"; done)
echo "Current major version $current_ver"
major_nex_ver=`echo $current_ver + 0.01 | bc`
next_ver=$(apt-cache madison kubeadm | grep ${major_nex_ver} | head -n 1 |  awk '{print $3}')
echo "Next version $next_ver"
nodename=$(hostname)
echo "Hostname $nodename"

echo "netapp1!" | sudo -S  apt-mark unhold kubeadm && \
sudo apt-get update &&  sudo apt-get install -y kubeadm=$next_ver && \
sudo apt-mark hold kubeadm

echo "netapp1!" | sudo -S  kubeadm version
echo "netapp1!" | sudo -S  kubeadm upgrade plan --ignore-preflight-errors=all

apply_ver=$(echo "${next_ver:0:-3}")
echo "netapp1!" | sudo -S  kubeadm upgrade apply -y v$apply_ver --ignore-preflight-errors=all --force

echo "netapp1!" | sudo -S  kubectl drain $nodename --ignore-daemonsets --delete-local-data

echo "netapp1!" | sudo -S  apt-mark unhold kubelet kubectl && \
echo "netapp1!" | sudo -S  apt-get update && sudo apt-get install -y kubelet=$next_ver kubectl=$next_ver && \
echo "netapp1!" | sudo -S  apt-mark hold kubelet kubectl

echo "netapp1!" | sudo -S  systemctl daemon-reload
echo "netapp1!" | sudo -S  systemctl restart kubelet

# replace <cp-node-name> with the name of your control plane node
echo "netapp1!" | sudo -S  kubectl uncordon $nodename

echo "${next_ver}"

sudo kubectl get node 
