from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
import Assistent
import sys


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<--', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        for_btn = QAction('-->', self)
        for_btn.triggered.connect(self.browser.forward)
        navbar.addAction(for_btn)

        rel_btn = QAction('^', self)
        rel_btn.triggered.connect(self.browser.reload)
        navbar.addAction(rel_btn)

        home = QAction('Home', self)
        home.triggered.connect(self.nav_home)
        navbar.addAction(home)


        test_btn = QAction('Test', self)
        test_btn.setText("Dev1l Browser")
        test_btn.triggered(self.browser.setUrl(QUrl('')))
        navbar.addAction(test_btn)


        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_url)
        navbar.addWidget(self.url_bar)


        self.browser.urlChanged.connect(self.updated_url)
    def nav_home(self):
        self.browser.setUrl(QUrl('https://google.com/'))
    def nav_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def updated_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Dev1l')
window = Main()
app.exec_()
Assistent.Assistant.start_up()

