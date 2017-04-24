import sys
import random
import requests
import json

from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
import time

def getEvent(url_path, key) :
    responseString = ""
 
    params = {'city':city, 'key':key,'topic':topic}
    r = requests.get(url_path, params = params)    
    print(r.url)    
    responseString = r.text
    return responseString

app = QApplication(sys.argv)

browser = QWebView()

url_path = "https://api.meetup.com"         #Url to meetup API
key_path = "api_key.txt"                    #Path to api_key.txt
path_code = ""                              #var to store the url_path + the specific api path
key = "d6d2d4d3718361f7b5a4f63201b7162"     #key for junk account    

params = {'key':key}

while True:
    response = eg.getEvent("https://api.meetup.com/Freeside-Atlanta/events", key)
    r = requests.get(url_path, params = params)
    print(r.url)    
    response = r.text
    events = decodeJSON(response)
    
    for event in events:
        browser.load(QUrl(event["link"]))
        browser.show()
        time.sleep(30)

app.exec_()
