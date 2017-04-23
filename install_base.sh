# updates and stuff
sudo apt-get update
sudo apt-get upgrade

#keep screen on and remove cursor if no movment
sudo apt-get install unclutter

#enable ssh
sudo touch /boot/ssh

#install photo reel dependencies
sudo apt-get install python-opencv

#move our stuff to a better spot
sudo mkdir -p /usr/local/bin
sudo cp -r ../FreesideScreen /usr/local/bin

#remove annoying thing asking us to change password
sudo rm /etc/xdg/lxsession/LXDE-pi/sshpwd.sh
