#!/usr/bin/bash


###################
# System settings #
###################
sudo timedatectl set-timezone Europe/Moscow
echo "timezone is set"


###########################
# Configuring vla profile #
###########################
sh -c "cat >> /home/vla/.bashrc" << EOL

# ignore for some regular commands
HISTIGNORE="clear:exit:pwd:cd *:touch *:man *:ll:top:top -u vla:ip a:ip neigh show*:speedtest --single"
HISTIGNORE=":\$HISTIGNORE:crontab -e:sudo crontab -e:*--help:ifconfig:ssh*:offf*:reee*:*.bashrc"
HISTIGNORE=":\$HISTIGNORE:*.bash_history:*.bash_aliases:*/etc/fstab:updateit*:upgradeit*:sudo mount -va"
HISTIGNORE=":\$HISTIGNORE:lsblk:python:python3:py:which *:pip3 list*:source*:deactivate"
EOL
source "/home/vla/.bashrc"
echo "vla .bashrc is set"


#####################################
# Configuring vla profile (aliases) #
#####################################
sh -c "cat > /home/vla/.bash_aliases" << EOL
# routine
alias updateit='sudo apt update && apt list --upgradable'
alias upgradeit='sudo apt upgrade -y'
# power management
alias offf='sudo systemctl poweroff'
alias reee='sudo systemctl reboot'
# misc
alias py='python3'
EOL
source "/home/vla/.bash_aliases"
echo "vla .bash_aliases is set"


################
# Adding users #
################
sudo adduser operator
sudo adduser himg
sudo adduser tvv
sudo adduser sde


######################
# Creating /srv tree #
######################
sudo mkdir --verbose /mnt/{R,rdump,jrcnav{m,r},F}
sudo mkdir --verbose --parents \
	/home/operator/.creds \
	/srv/A2/{R,hub,top} \
	/srv/lcontainer/{hagrid,hedwig,irma,filch,sndbx,init} \
	/srv/lcontainer/filch/MIB \
	/srv/{development,dump,imgs}
sudo chown --changes operator:operator \
	/home/operator/.creds \
	/srv/dump /srv/A2/R \
	/srv/lcontainer/{hagrid,hedwig,irma,filch} \
	/srv/lcontainer/filch/MIB


####################################
# Creating credentials environment #
####################################
sudo -su operator nano /home/operator/.creds/.tlg_id_lngd
sudo -su operator nano /home/operator/.creds/.tlg_bot_serverbot
sudo -su operator nano /home/operator/.creds/.tlg_bot_RMPMRMGMDSSBOT
sudo -su operator nano /home/operator/.creds/.tlg_bot_RMPMRMTECHBOT
sudo -su operator nano /home/operator/.creds/.tlg_channel_RMPMRMGMDSS
sudo -su operator nano /home/operator/.creds/.tlg_channel_RMPMRMTECH
sudo -su operator nano /home/operator/.creds/.token_mail_mtf.udk


###########################################
# Maintaining /srv and credentials access #
###########################################
sudo chown --changes vla:vla /srv/development
sudo chown --changes himg:himg /srv/imgs
sudo chmod --changes 400 /home/operator/.creds/.tlg_id_lngd
sudo chmod --changes 400 /home/operator/.creds/.tlg_bot_serverbot
sudo chmod --changes 400 /home/operator/.creds/.tlg_bot_RMPMRMGMDSSBOT
sudo chmod --changes 400 /home/operator/.creds/.tlg_bot_RMPMRMTECHBOT
sudo chmod --changes 400 /home/operator/.creds/.tlg_channel_RMPMRMGMDSS
sudo chmod --changes 400 /home/operator/.creds/.tlg_channel_RMPMRMTECH
sudo chmod --changes 400 /home/operator/.creds/.token_mail_mtf.udk
sudo chmod --changes 100 /home/operator/.creds
sudo chmod --changes 777 /srv/dump /srv/lcontainer/sndbx /srv/A2/R /mnt/{R,rdump,jrcnav{m,r}}


######################################
# Downloading pygwarts for operator #
######################################
sudo -su operator git clone \
	https://github.com/longdeer/pygwarts.git \
	/home/operator/.local/lib/python3.12/site-packages/pygwarts


###############################################
# Downloading NavtexBoWAnalyzer for operator #
###############################################
sudo -su operator git clone \
	https://github.com/longdeer/NavtexBoWAnalyzer.git \
	/home/operator/.local/lib/python3.12/site-packages/NavtexBoWAnalyzer


############################
# Downloading hagrid files #
############################
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/navtex_preprocessor.py \
	-O /srv/lcontainer/hagrid/navtex_preprocessor.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/rmp_arch.py \
	-O /srv/lcontainer/hagrid/arch.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/rmp_softsync.py \
	-O /srv/lcontainer/hagrid/softsync.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/rmp_hardsync.py \
	-O /srv/lcontainer/hagrid/hardsync.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/rmp_navdrop.py \
	-O /srv/lcontainer/hagrid/navdrop.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/rmp_navbow.py \
	-O /srv/lcontainer/hagrid/navbow.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hagrid/rmp_unittest_navbow.py \
	-O /srv/lcontainer/hagrid/unittest_navbow.py


###########################
# Downloading filch files #
###########################
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/filch/rmp_discovery.py \
	-O /srv/lcontainer/filch/discovery.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/filch/rmp_broadwatch.py \
	-O /srv/lcontainer/filch/broadwatch.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/filch/rmp_snmpwatch.py \
	-O /srv/lcontainer/filch/snmpwatch.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/DS1-MIB.py \
	-O /srv/lcontainer/filch/MIB/DS1-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/IANAifType-MIB.py \
	-O /srv/lcontainer/filch/MIB/IANAifType-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/IF-MIB.py \
	-O /srv/lcontainer/filch/MIB/IF-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/POLYCOM740-MIB.py \
	-O /srv/lcontainer/filch/MIB/POLYCOM740-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/POLYGON-MIB.py \
	-O /srv/lcontainer/filch/MIB/POLYGON-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/PerfHist-TC-MIB.py \
	-O /srv/lcontainer/filch/MIB/PerfHist-TC-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/RS-232-MIB.py \
	-O /srv/lcontainer/filch/MIB/RS-232-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/SNMP-COMMUNITY-MIB.py \
	-O /srv/lcontainer/filch/MIB/SNMP-COMMUNITY-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/SNMPv2-MIB.py \
	-O /srv/lcontainer/filch/MIB/SNMPv2-MIB.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/snmp/XPPC-MIB.py \
	-O /srv/lcontainer/filch/MIB/XPPC-MIB.py


##########################
# Downloading irma files #
##########################
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/irma/rmp_library.py \
	-O /srv/lcontainer/irma/library.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/irma/rmp_intercept.py \
	-O /home/operator/.local/lib/python3.12/site-packages/irma_local_intercept.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/irma/rmp_access.py \
	-O /home/operator/.local/lib/python3.12/site-packages/irma_local_access.py


############################
# Downloading hedwig files #
############################
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/pygwarts-exp/refs/heads/master/hedwig/rmp_report.py \
	-O /srv/lcontainer/hedwig/report.py


################################
# Downloading additional files #
################################
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/tools/credistr.py \
	-O /home/operator/.local/lib/python3.12/site-packages/credistr.py
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/text/scanner.py \
	-O /home/operator/.local/lib/python3.12/site-packages/lngd_local_scanner.py


#####################################
# Maintaining external files access #
#####################################
sudo chmod --changes 444 /srv/lcontainer/hagrid/navdrop.py
sudo chmod --changes 444 /srv/lcontainer/hagrid/hardsync.py
sudo chmod --changes 444 /srv/lcontainer/hagrid/softsync.py
sudo chmod --changes 444 /srv/lcontainer/hagrid/arch.py
sudo chmod --changes 444 /srv/lcontainer/hagrid/navtex_preprocessor.py
sudo chmod --changes 444 /srv/lcontainer/hagrid/navbow.py
sudo chmod --changes 444 /srv/lcontainer/hagrid/unittest_navbow.py
sudo chmod --changes 444 /srv/lcontainer/filch/discovery.py
sudo chmod --changes 444 /srv/lcontainer/filch/broadwatch.py
sudo chmod --changes 444 /srv/lcontainer/filch/snmpwatch.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/DS1-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/IANAifType-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/IF-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/POLYCOM740-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/POLYGON-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/PerfHist-TC-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/RS-232-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/SNMP-COMMUNITY-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/SNMPv2-MIB.py
sudo chmod --changes 444 /srv/lcontainer/filch/MIB/XPPC-MIB.py
sudo chmod --changes 444 /srv/lcontainer/irma/library.py
sudo chmod --changes 444 /srv/lcontainer/hedwig/report.py


###############################
# Configuring credentials API #
###############################
sudo -su operator sh -c "cat >> /home/operator/.local/lib/python3.12/site-packages/credistr.py" << EOL

tlg_id_lngd = lambda : cred("/home/operator/.creds/.tlg_id_lngd")
token_mail_mtfudk = lambda : cred("/home/operator/.creds/.token_mail_mtf.udk")
tlg_bot_serverbot = lambda : cred("/home/operator/.creds/.tlg_bot_serverbot")
tlg_bot_RMPMRMGMDSSBOT = lambda : cred("/home/operator/.creds/.tlg_bot_RMPMRMGMDSSBOT")
tlg_bot_RMPMRMTECHBOT = lambda : cred("/home/operator/.creds/.tlg_bot_RMPMRMTECHBOT")
tlg_channel_RMPMRMGMDSS = lambda : cred("/home/operator/.creds/.tlg_channel_RMPMRMGMDSS")
tlg_channel_RMPMRMTECH = lambda : cred("/home/operator/.creds/.tlg_channel_RMPMRMTECH")
EOL
echo "credentials API is set"


###################################################
# Downloading and tuning ARP cache manager script #
###################################################
sudo wget https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/network/L2/addneigh.sh \
	-O /srv/lcontainer/init/bootneigh.sh
sudo sh -c "cat >> /srv/lcontainer/init/bootneigh.sh" << EOL

addneigh "ip4 address" "mac address" "host name"
EOL
sudo chmod 700 /srv/lcontainer/init/bootneigh.sh


################################
# Mounting gserver dump folder #
################################
sudo mount //192.168.162.111/gdump /mnt/rdump -o guest,file_mode=0777,dir_mode=0777


####################################################################
# Copying current filch maps and Navtex BoW with access management #
####################################################################
sudo -su operator cp -v /mnt/rdump/*.csv -t /srv/lcontainer/filch
sudo -su operator cp -v /mnt/rdump/Navbag.Shelf /srv/lcontainer/hagrid
sudo chmod --changes 400 /srv/lcontainer/filch/*.csv
sudo chmod --changes 600 /srv/lcontainer/hagrid/Navbag.Shelf


###############################################################################
# Copying patched samba, bootstrapping, configuring and installing            #
# (it is crucial to bootstrap on the fresh OS so no dependencies will suffer) #
###############################################################################
echo "getting samba"
cp --recursive /mnt/rdump/samba-4.21.1-patched /srv/development/
echo "installing samba"
cd /srv/development/samba-4.21.1-patched
sudo bootstrap/generated-dists/ubuntu2204/bootstrap.sh
sudo ./configure \
	--prefix=/usr \
	--enable-fhs \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--with-privatedir=/var/lib/samba/private \
	--with-smbpasswd-file=/etc/samba/smbpasswd \
	--with-piddir=/var/run/samba \
	--with-pammodulesdir=/lib/x86_64-linux-gnu/security \
	--libdir=/usr/lib/x86_64-linux-gnu \
	--with-modulesdir=/usr/lib/x86_64-linux-gnu/samba \
	--datadir=/usr/share \
	--with-lockdir=/var/run/samba \
	--with-statedir=/var/lib/samba \
	--with-cachedir=/var/cache/samba \
	--with-socketpath=/var/run/ctdb/ctdbd.socket \
	--with-logdir=/var/log/ctdb \
	--systemd-install-services \
	--without-ad-dc
sudo make -j 4
sudo make install -j 4


#########################
# Creating samba config #
#########################
sudo sh -c "cat > /etc/samba/smb.conf" << EOL
[global]

   server min protocol = LANMAN2
   workgroup = radio
   server string = hserver (Samba, Ubuntu)
   log file = /var/log/samba/log.%m
   max log size = 1000
   logging = file
   panic action = /usr/share/samba/panic-action %d
   server role = standalone server
   obey pam restrictions = yes
   unix password sync = yes
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
   pam password change = yes
   map to guest = bad user
   usershare allow guests = yes

[printers]

   comment = All Printers
   browseable = no
   path = /var/spool/samba
   printable = yes
   guest ok = no
   read only = yes
   create mask = 0700

[print$]

   comment = Printer Drivers
   path = /var/lib/samba/printers
   browseable = yes
   read only = yes
   guest ok = no

[hdevelopment]

   comment = hserver development hub
   path = /srv/development
   valid users = vla
   guest ok = no
   create mask = 0777
   directory mask = 0777
   browseable = yes
   writeable = yes
   read only = no

[hdisk]

   comment = hserver A2 GMDSS R and share
   path = /srv/A2/R
   guest ok = yes
   browseable = yes
   writeable = yes
   read only = no
   force user = operator
   force group = operator

[hhub]

   comment = hserver hub ops use
   path = /srv/A2/hub
   valid users = vla,tvv,sde
   guest ok = no
   create mask = 0777
   directory mask = 0777
   browseable = yes
   writeable = yes
   read only = no

[htop]

   comment = hserver authority
   path = /srv/A2/top
   valid users = vla,tvv
   guest ok = no
   create mask = 0777
   directory mask = 0777
   browseable = yes
   writeable = yes
   read only = no

[CIRCUL]

   comment = CKS/ARQ/OUT mountable
   path = /srv/A2/R/CKS/ARQ/OUT/CIRCUL
   guest ok = yes
   browseable = yes
   writeable = yes
   read only = no
   force user = operator
   force group = operator

[INMC]

   comment = CKS/INMSAT_C mountable
   path = /srv/A2/R/CKS/INMSAT_C
   guest ok = yes
   browseable = yes
   writeable = yes
   read only = no
   force user = operator
   force group = operator

[NAVTEX]

   comment = CKS/ARQ/NAVTEX mountable
   path = /srv/A2/R/CKS/ARQ/NAVTEX
   guest ok = yes
   browseable = yes
   writeable = yes
   read only = no
   force user = operator
   force group = operator

[hdump]

   comment = hserver dump
   path = /srv/dump
   guest ok = yes
   browseable = yes
   writeable = yes
   read only = no
   force user = operator
   force group = operator

[himgs]

   comment = hserver backups storage
   path = /srv/imgs
   valid users = himg
   guest ok = no
   create mask = 0700
   directory mask = 0700
   browseable = yes
   writable = yes
   read only = no
EOL
echo "smb.conf is set"


#######################################################
# Turning on samba services (with name sever for DOS) #
#######################################################
sudo systemctl enable smb.service
sudo systemctl enable nmb.service
sudo systemctl start smb.service
sudo systemctl start nmb.service


#####################################
# Creating and enabling samba users #
#####################################
echo "adding samba user operator"
sudo smbpasswd -a operator
sudo smbpasswd -e operator
echo "adding samba user vla"
sudo smbpasswd -a vla
sudo smbpasswd -e vla
echo "adding samba user tvv"
sudo smbpasswd -a tvv
sudo smbpasswd -e tvv
echo "adding samba user sde"
sudo smbpasswd -a sde
sudo smbpasswd -e sde
echo "adding samba user himg"
sudo smbpasswd -a himg
sudo smbpasswd -e himg


##############################################
# Mounting and replicating current gserver R #
##############################################
sudo mount //192.168.162.111/gdisk /mnt/R -o guest,file_mode=0777,dir_mode=0777
echo "replicating R"
sudo -su operator cp --recursive /mnt/R/* -t /srv/A2/R
echo "done replicating R"


#############################################################
# Installing additional packages and Python3.10 (with venv) #
# for filch and configuring it to work well                 #
#############################################################
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install tree iftop cifs-utils net-tools python3-venv python3-matplotlib python3.10 python3.10-venv
sudo -su operator python3.10 -m venv --copies /srv/lcontainer/sndbx/v-filch
sudo cp /bin/tcpdump /srv/lcontainer/sndbx/v-filch/bin
sudo chown --changes operator:operator /srv/lcontainer/sndbx/v-filch/bin/tcpdump
sudo chmod --changes 700 /srv/lcontainer/sndbx/v-filch/bin/tcpdump
sudo chmod --changes 700 /srv/lcontainer/sndbx/v-filch/bin/python*
sudo setcap "cap_net_raw=eip cap_net_bind_service=eip" /srv/lcontainer/sndbx/v-filch/bin/python3
sudo -su operator /srv/lcontainer/sndbx/v-filch/bin/pip install \
	scapy==2.5.0rc3 pyasn1==0.4.8 pysmi==0.3.4 pysnmp==4.4.11
sudo -su operator ln -s /home/operator/.local/lib/python3.12/site-packages/pygwarts \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /home/operator/.local/lib/python3.12/site-packages/irma_local_intercept.py \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /usr/lib/python3/dist-packages/requests \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /usr/lib/python3/dist-packages/urllib3 \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /usr/lib/python3/dist-packages/chardet \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /usr/lib/python3/dist-packages/certifi \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /usr/lib/python3/dist-packages/idna \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/
sudo -su operator ln -s /home/operator/.local/lib/python3.12/site-packages/credistr.py \
	/srv/lcontainer/sndbx/v-filch/lib/python3.10/site-packages/


########################################
# Configuring filch broadwatch service #
########################################
sudo -su operator sh -c "cat > /srv/lcontainer/filch/filch-broadwatch.service" << EOL
[Unit]
Description=filch broadwatch
After=network.target

[Service]
Restart=always
RestartSec=60
User=operator
ExecStart=/srv/lcontainer/sndbx/v-filch/bin/python3 /srv/lcontainer/filch/broadwatch.py

[Install]
WantedBy=multi-user.target
EOL
sudo ln -s /srv/lcontainer/filch/filch-broadwatch.service /etc/systemd/system/
sudo systemctl enable filch-broadwatch.service
sudo systemctl start filch-broadwatch.service


#######################################
# Configuring filch snmpwatch service #
#######################################
sudo -su operator sh -c "cat > /srv/lcontainer/filch/filch-snmpwatch.service" << EOL
[Unit]
Description=filch snmpwatch
After=network.target

[Service]
Restart=always
RestartSec=90
User=operator
ExecStart=/srv/lcontainer/sndbx/v-filch/bin/python3 /srv/lcontainer/filch/snmpwatch.py

[Install]
WantedBy=multi-user.target
EOL
sudo ln -s /srv/lcontainer/filch/filch-snmpwatch.service /etc/systemd/system/
sudo systemctl enable filch-snmpwatch.service
sudo systemctl start filch-snmpwatch.service


#############################################
# Installing server controller telegram bot #
#############################################
sudo -su operator python3 -m venv --system-site-packages --symlinks \
	/srv/lcontainer/sndbx/v-server-controller
sudo -su operator /srv/lcontainer/sndbx/v-server-controller/bin/pip install telebot
sudo -su operator wget \
	https://raw.githubusercontent.com/longdeer/exp/refs/heads/master/telegram/server_controller.py \
	-O /srv/lcontainer/sndbx/v-server-controller/server_controller.py
sudo -su operator ln -s /srv/lcontainer/hagrid/navbow.py /srv/lcontainer/sndbx/v-server-controller/
sudo -su operator sh -c "cat > /srv/lcontainer/sndbx/v-server-controller/hserver-controller.service" << EOL
[Unit]
Description=hserver controller telegram bot
After=network.target

[Service]
Restart=always
RestartSec=90
User=operator
ExecStart=/srv/lcontainer/sndbx/v-server-controller/bin/python3 /srv/lcontainer/sndbx/v-server-controller/server_controller.py

[Install]
WantedBy=multi-user.target
EOL
sudo ln -s /srv/lcontainer/sndbx/v-server-controller/hserver-controller.service /etc/systemd/system/
sudo systemctl enable hserver-controller.service
sudo systemctl start hserver-controller.service


###################################
# Configuring operator cron jobs #
###################################
sudo -su operator sh -c "crontab -" << EOL
10-59 0 * * * cd /srv/lcontainer/hagrid && /usr/bin/python3 navdrop.py >> hagrid.cronloggy 2>&1
* 1-23 * * * cd /srv/lcontainer/hagrid && /usr/bin/python3 navdrop.py >> hagrid.cronloggy 2>&1
10-59/5 0 * * * cd /srv/lcontainer/hagrid && /usr/bin/python3 softsync.py >> hagrid.cronloggy 2>&1
*/5 1-23 * * * cd /srv/lcontainer/hagrid && /usr/bin/python3 softsync.py >> hagrid.cronloggy 2>&1
1 0 * * * cd /srv/lcontainer/hagrid && /usr/bin/python3 hardsync.py >> hagrid.cronloggy 2>&1
10 0 * * * cd /srv/lcontainer/irma && /usr/bin/python3 library.py >> irma.cronloggy 2>&1 && cd /srv/lcontainer/hedwig && /usr/bin/python3 report.py >> hedwig.cronloggy 2>&1
57 23 * * * cd /srv/lcontainer/hagrid && /usr/bin/python3 arch.py >> hagrid.cronloggy 2>&1
1 23 * * * cd /srv/lcontainer/filch && /srv/lcontainer/sndbx/v-filch/bin/python3 discovery.py >> filch.cronloggy 2>&1
EOL
echo "operator cronjobs are set (minimal)"


##############################
# Adding hserver fstab rules #
##############################
echo "//192.168.162.111/gdisk /mnt/R cifs guest,file_mode=0777,dir_mode=0777 0 0" \
	| sudo tee --append /etc/fstab
echo "//192.168.162.111/gdump /mnt/rdump cifs guest,file_mode=0777,dir_mode=0777 0 0" \
	| sudo tee --append /etc/fstab
echo "//192.168.161.10/navmdrop /mnt/jrcnavm cifs password=,file_mode=0777,dir_mode=0777 0 0" \
	| sudo tee --append /etc/fstab
echo "//192.168.161.30/navrdrop /mnt/jrcnavr cifs password=,file_mode=0777,dir_mode=0777 0 0" \
	| sudo tee --append /etc/fstab


############################################################################################
# Configuring hserver netplan (better be invoked manually with interfaces names specified) #
############################################################################################
echo "network: {config: disabled}" | sudo tee /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg
sudo rm -v /etc/netplan/*
sudo sh -c "cat > /etc/netplan/hserver-netplan.yaml" << EOL
network:
    ethernets:
        eno1:
            dhcp4: no
            addresses:
            - 192.168.162.222/22
            - 192.168.162.200/22
            nameservers:
                addresses:
                - 192.168.0.2
                search: []
            routes:
            - to: 192.168.160.0/22
        eno2:
            dhcp4: no
            addresses:
            - 192.168.0.200/24
            routes:
            - to: default
              via: 192.168.0.2
            nameservers:
                addresses:
                - 192.168.0.2
    version: 2
EOL
echo "netplan is set"

