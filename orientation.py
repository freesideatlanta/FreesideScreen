import cv2
from os import listdir
from os.path import isfile, join

cv2.namedWindow("main", cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty("main", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)


path = "/usr/local/bin/FreesideScreen/orientation"
while(True):
	try:
		filenames = listdir(path)
		filenames.sort(key=lambda f: int(filter(str.isdigit, f)))
		for f in filenames:
			full_path = join(path, f)
			if not isfile(full_path):
				continue
			img = cv2.imread(full_path, cv2.CV_LOAD_IMAGE_COLOR);

			cv2.imshow("main",img)
			if cv2.waitKey(8000) & 0xff == 27: quit()
	except Exception as e:
		print "rror", e
