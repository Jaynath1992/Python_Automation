#!/bin/bash -xe

# Get the ip on which timescale has been installed from the user

echo " Enter the ip address of the machine on which timescale is installed"

read ip 


#Replace the host ip on the pgbouncer.ini with the ip provided by the user

echo " Replace the host ip on the pgbouncer with ip provided by user to obtain the secret key"


sed "2s/x.x.x.x/$ip/" -i  pgbouncer.ini
sed "3s/x.x.x.x/$ip/" -i pgbouncer.ini
sed "4s/x.x.x.x/$ip/" -i pgbouncer.ini


#Obtain the secret key and store it in a variable

secret_key=`cat pgbouncer.ini | base64 -w 0`  

#Patch the pgbouncer-config to reflect the obtained secret key

kubectl patch secret pgbouncer-config -p="{\"data\":{\"pgbouncer.ini\": \"${secret_key}\"}}"

#Restart the pgbouncer pods
kubectl get pods | grep pgbouncer | awk '{print $1}' | xargs kubectl delete pod
