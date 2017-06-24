import cv2
import urllib
import numpy as np
import random
import time
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
from os import listdir

from os.path import isfile, join

cv2.namedWindow("main", cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty("main", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)


#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()

#drive = GoogleDrive(gauth)


# fix by authing here https://script.google.com/d/1jX5iS0ofuh8fjbDMBdGk7C6uQDa8xveN5sleiCBRgdOkUEbECxgYIupg/edit?usp=drive_web
# on account freesideprogramming@gmail.com

path = "/usr/local/bin/FreesideScreen/orientation"
while(True):
	try:
		filenames = listdir(path)
		filenames = filenames.sort(key=lambda f: int(filter(str.isdigit, f)))
		for f in listdir(path):
			full_path = join(path, f)
			if not isfile(full_path):
				continue
			img = cv2.imread(full_path, cv2.CV_LOAD_IMAGE_COLOR);

			cv2.imshow("main",img)
			if cv2.waitKey(8000) & 0xff == 27: quit()
	except Exception as e:
		print "rror", e
