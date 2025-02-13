#!/bin/bash  -xe

echo "Information regarding the hostname and Linux Ubuntu version"
hostnamectl

echo " Storage used/available on the machine"
df -h

echo " Installation of Timescale VM"

# Install timescaledb
echo " Install timescale "
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -c -s)-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo add-apt-repository ppa:timescale/timescaledb-ppa

sudo apt-get update

# Install timescaledb on postgresql
sudo apt install timescaledb-postgresql-12


# Restart postgresql service
sudo service postgresql restart



echo " Update the configurations on the pg_hba.conf file"

# Switch to /etc/postgresql/12/main and edit the pg_hba.conf

cd /etc/postgresql/12/main/

# Comment out the existing configurations

sed -e' /local/s/^#*/#/g' -i pg_hba.conf
sed -e' /host/s/^#*/#/g' -i pg_hba.conf

# Add the following configurations into the pg_hba.conf file

sed '$ a local     all             postgres                                peer' -i pg_hba.conf
sed '$ a local     all             all                                     md5' -i  pg_hba.conf
sed '$ a hostnossl all,replication all                all                  reject' -i  pg_hba.conf
sed '$ a hostssl   all             all                127.0.0.1/32         md5' -i  pg_hba.conf
sed '$ a hostssl   all             all                ::1/128              md5' -i  pg_hba.conf
sed '$ a hostssl   replication     standby            all                  md5' -i  pg_hba.conf
sed '$ a hostssl   all             all                all                  md5' -i  pg_hba.conf


echo " Configure the listen_address on postgresql.conf file to allow the DB to listen to all hosts on the network" 

# Configure the postgresql.conf file to allow listen_address to listen to all hosts

sed -i '/listen_addresses/s/^#//g' postgresql.conf
sed '60s/localhost/*/' -i postgresql.conf

# Restart postgresql service
sudo service postgresql restart
