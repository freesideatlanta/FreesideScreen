# updates and stuff
sudo apt-get update
sudo apt-get -y upgrade

#keep screen on and remove cursor if no movment
sudo apt-get install -y unclutter

#enable ssh
sudo touch /boot/ssh

#install photo reel dependencies
sudo apt-get install -y python-opencv

#move our stuff to a better spot
sudo mkdir -p /usr/local/bin
sudo cp -r ../FreesideScreen /usr/local/bin

#remove annoying thing asking us to change password
sudo rm /etc/xdg/lxsession/LXDE-pi/sshpwd.sh &
sudo rm /etc/xdg/lxsession/LXDE/sshpwd.sh &

#attempt to change the keyboard layout
sudo cp tools/keyboard /etc/default/keyboard
invoke-rc.d keyboard-setup start

#Do a number of things
#including trying again to keep the screen from blanking
sudo cp tools/.bashrc /home/pi/.bashrc
