#!/usr/bin/env bash

sudo apt update
sudo apt install sqlite3
sudo pip3 install requests
sudo pip3 install python-firebase

#git clone
if [ ! -d /home/pi/Desktop/trafis_project ]
then
    sudo git clone https://gitlab.com/aruna_iot/trafis_project.git
else
    cd trafis_project/
    sudo git pull
    cd ..
fi


#run crontab
sudo crontab -l > mycron

add() {
  grep -Fq "$1" mycron || echo "$1" >> mycron
}

add "*/3 * * * * home/pi/Desktop/trafis_project/main.py 1"
add "*/15 * * * * home/pi/Desktop/trafis_project/main.py 2"
crontab mycron
rm mycron
