cd /usr/local/bin/FreesideScreen

# run even if this fails
# should be ok to not be connected to the internet
git fetch &
sleep 2
git pull &

# wait until everything boots up
sleep 8
python /usr/local/bin/FreesideScreen/show.py
