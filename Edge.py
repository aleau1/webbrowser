#!/usr/bin/env python 3.11.2
from webbrowser.WebBrowser import WebBrowser

class Edge(WebBrowser):
    def __init__(self):
        super().__init__("C:\\Program Files (x86)\\Microsoft\\Edge\\Application", 'msedge.exe')


if __name__=="__main__":
    raise NotImplementedError()

