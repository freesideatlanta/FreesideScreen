# From
# https://superuser.com/questions/873381/how-can-i-disable-the-chromium-didn-t-shut-down-correctly-message-when-my-brow


# Chromium version 39 (on Ubuntu at least) tracks the browser's exit state in three separate files:
# 
# ~/.config/chromium/"Profile 1"/Preferences
# ~/.config/chromium/"Profile 1"/.org.chromium.Chromium.XXXXXX
# ~/.config/chromium/"Local State"
# Where "XXXXXX" is a six-digit random alphanumeric string. Note also that "Profile 1" may be named differently based on what browser profile you are using (another common profile name is simply "Default")
# 
# The two profile-based files have two entries that can trigger the message, "exit_state" (values are either "Normal" or "Crashed", with quotes) and "exited_cleanly" (values are either true or false, without quotes).
# 
# The "Local State" file only contains the "exited_cleanly" entry.
# 
# There is also a "lock" file that may cause trouble; this file is located at
# 
# ~/.config/chromium/SingletonLock



#!/bin/bash

#Set CrProfile to the value of your startup profile's config folder
#From ref'd web page, commented
#CrProfile="Profile 1"
CrProfile="Default"


#Set URL to the URL that you want the browser to start with

#From ref'd web page, commented
URL="https://freesideatlanta.slack.com/x-173160447363-174051129031/signin"

#Clean up the randomly-named file(s)
for i in $HOME/.config/chromium/$CrProfile/.org.chromium.Chromium.*; do
    sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' $i
    sed -i 's/"exit_state": "Crashed"/"exit_state": "Normal"/' $i
done

#Clean up Preferences
sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' $HOME/.config/chromium/$CrProfile/Preferences
sed -i 's/"exit_state": "Crashed"/"exit_state": "Normal"/' $HOME/.config/chromium/$CrProfile/Preferences

#Clean up Local State
sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' $HOME/.config/chromium/"Local State"

#Delete SingletonLock
rm -f $HOME/.config/chromium/SingletonLock

#From ref'd web page, commented
/usr/bin/chromium-browser --kiosk $URL

/bin/sleep 1

#From Nathan's autostart_slack file, with leading "@" removed
