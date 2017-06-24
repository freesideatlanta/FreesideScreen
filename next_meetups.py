import sys
import random
import requests
import json

from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
import time


class Browser(QWebView):

    def __init__(self):
        QWebView.__init__(self)
        self.loadFinished.connect(self._result_available)
        self.events = []
        self.goto_link()

    def _result_available(self, ok):
        frame = self.page().mainFrame()
        self.show()
        #print unicode(frame.toHtml()).encode('utf-8')
        time.sleep(10)
        self.goto_link()

    def goto_link(self):
        if(len(self.events)==0):
            self.get_events()

        event = self.events.pop(0)

        link = event["link"]
        print link
        self.load(QUrl(link))

    def get_events(self):
        r = requests.get("https://api.meetup.com/Freeside-Atlanta/events", params = {'key':"d6d2d4d3718361f7b5a4f63201b7162"} )
        print(r.url)
        response = r.text
        self.events = json.loads(response)[:10]

app = QApplication(sys.argv)

browser = Browser()

app.exec_()
