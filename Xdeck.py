import sys
import os
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QApplication)
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class PersephoneWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # レイアウト
        boxLayout = QHBoxLayout()

        # カラム数
        self.addColumn(boxLayout)
        self.addColumn(boxLayout)
        self.addColumn(boxLayout)
        
        self.setLayout(boxLayout) 
        self.setWindowTitle("TDeck")
        self.showMaximized()
        
    def addColumn(self, layout):
        
        # ブラウザ設定
        browser = QWebEngineView()
        browser.load(QUrl("https://twitter.com/home"))
        browser.setWindowTitle("TDeck")
        
        layout.addWidget(browser)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = PersephoneWindow()
    sys.exit(app.exec_())
