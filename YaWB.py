"""
Project Structure

1. Installing PyQt5 and PyQt5WebEngine
2. Importing modules & libraries
3. Creating a class
4. Creating various buttons on the top of the window
5. App Initialization
"""

# 2. Importing modules & libraries
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

# 3. Creating a class
class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('https://search.brave.com/'))
        self.setCentralWidget(self.Browser)
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('./images/browser_brave_icon_157736.ico'))
        NavBar = QToolBar()
        self.addToolBar(NavBar)

        # 4. Creating various buttons on the top of the window
        BackButton = QAction('Back', self)
        BackButton.triggered.connect(self.Browser.back)
        NavBar.addAction(BackButton)
 
        ForwardButton = QAction('Forward', self)
        ForwardButton.triggered.connect(self.Browser.forward)
        NavBar.addAction(ForwardButton)
 
        ReloadButton = QAction('Reload', self)
        ReloadButton.triggered.connect(self.Browser.reload)
 
        NavBar.addAction(ReloadButton)
        HomeButton = QAction('Home', self)
        HomeButton.triggered.connect(self.NavigateHome)

        self.UrlBar=QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavigateToUrl)
 
        NavBar.addWidget(self.UrlBar)
        self.Browser.urlChanged.connect(self.UpdateUrl)
 
# 5. App Initialization
    def NavigateHome(self):
        self.Browser.setUrl('https://search.brave.com/')
 
    def NavigateToUrl(self):
        Url = self.UrlBar.text()
        self.Browser.setUrl(QUrl('https://search.brave.com/'))
        
    def UpdateUrl(self,p):
        self.UrlBar.setText(str(p))
 
Application = QApplication(sys.argv)
QApplication.setApplicationName('Bravebone Web Browser')
Window = MainScreen()
Application.exec()
