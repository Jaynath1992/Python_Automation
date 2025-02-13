#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
    echo "You are logged in as $(id -u -n). Please sudo su and become root to run this script."
    exit
fi


echo "Shut down the system by stopping the kubelet on the target node"
systemctl stop kubelet;
echo "Remove all the docker containers"
docker rm -f -v $(docker ps -q);
echo "restart docker service"
systemctl restart docker.service
#find /var/lib/kubelet | xargs -n 1 findmnt -n -t tmpfs -o TARGET -T | uniq | xargs -r umount -v;
#sudo kubeadm reset --skip-preflight-checks   # uninstall 1.7.5
echo "undo all changes by kubeadm reset"
sudo kubeadm reset -f --ignore-preflight-errors=all #uninstall 1.10.6/1.12.8
echo "removing kuberenets completely"
sudo apt-get purge -y kubeadm kubectl kubelet kubernetes-cni --allow-change-held-packages
sudo apt-get autoremove -y kubeadm kubectl kubelet kubernetes-cni --allow-change-held-packages
echo "removing files/folders"
sudo rm -rf ~/.kube /etc/kubernetes /etc/systemd/system/kubelet.service.d /var/lib/kubelet /var/lib/etcd /var/lib/weave /mnt/cvspvc/;
reboot
