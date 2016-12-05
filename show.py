import cv2
import urllib
import numpy as np
import random
import time
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive

cv2.namedWindow("main", cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty("main", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)


#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()

#drive = GoogleDrive(gauth)


# fix by authing here https://script.google.com/d/1jX5iS0ofuh8fjbDMBdGk7C6uQDa8xveN5sleiCBRgdOkUEbECxgYIupg/edit?usp=drive_web
# on account freesideprogramming@gmail.com

url = "https://script.google.com/macros/s/AKfycbxYHSUWN2RHJz-5-qvjxcRDZn2bsdgnGDJ4KpnN3QHoc5yzuJk5/exec"
data = urllib.urlopen(url).read(20000).strip().split("\n")
print len(data)
print data
full = len(data)
while(True):

	try:
                print "full", full
		if len(data) == 0:
			data = urllib.urlopen(url).read(20000).strip().split("\n")
			print len(data)
			print data
		pick = (random.choice(data))
		data.remove(pick)
		print pick
		req = urllib.urlopen(pick)
		arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
		img = cv2.imdecode(arr,-1)

                print "LEN", len(arr)

		#file3 = drive.CreateFile({'id': '0B4F_8qOjRWueVXMwdmRoeWMzYUE'})
		#print 'Downloading file %s from Google Drive' % file3['title'] 
		#file3.GetContentFile('img/'+ file3['title'])

		#image = cv2.imread("img/"+file3['title'], cv2.CV_LOAD_IMAGE_COLOR);

		cv2.imshow("main",img)
		if cv2.waitKey(2000) & 0xff == 27: quit()
	except Exception as e:
		print "rror", e
