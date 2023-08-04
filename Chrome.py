#!/usr/bin/env python 3.11.2
from webbrowser.WebBrowser import WebBrowser

class Chrome(WebBrowser):
    def __init__(self):
        super().__init__("C:\\Program Files\\Google\\Chrome\\Application", 'chrome.exe')


if __name__=="__main__":
    raise NotImplementedError()

