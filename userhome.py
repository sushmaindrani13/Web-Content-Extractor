# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'userhome.ui'
# Created by: PyQt5 UI code generator 5.11.3
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import urllib.request
from nltk.tokenize import sent_tokenize
from inscriptis import get_text
from PyQt5 import QtCore, QtGui, QtWidgets
from urlaction import URLCheck
from tfidf import TFIDF
import os
import bs4
import pymysql.cursors
          
class userhome(object):
    def geturl(self):
        try:
            print("url")
            urlvar = self.url.text()
            print("url=", urlvar)
            u = URLCheck()
            res = URLCheck.validation(urlvar)
            if res == True:
                self.process(urlvar)
                
            else:
                self.showAlertBox("Data Alert", "       Enter Valid URL     ")

        except Exception as e:
            print("try1")
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def process(self,url):
        try:
            print("in process")
            cont= self.cont.text()
            connection = pymysql.connect(host='localhost',
                             user='root',
                             password='divya',
                             db='wce',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                # Read a single record
                    sql = "SELECT `content` FROM `data` WHERE `url`=%s and `keyword`=%s"
                    cursor.execute(sql, (url,cont))
                    result = cursor.fetchone()
                    print("Database Result=",result)
                    if(result!=None):
                        out="FROM DATABASE :\n"+result['content']
                        f=open("output.html","w")
                        f.write(out)
                        f.close()
                        import webbrowser
                        print(url)
                        webbrowser.open_new_tab(url)
                        webbrowser.open_new("output.html")
                        self.showAlertBox("Alert", "       Operation Done     ")
                        return
            finally:
                connection.close()
            html = urllib.request.urlopen(url).read().decode('utf-8')
            if ("wikipedia" in url):
                print("WIKI")
                code=bs4.BeautifulSoup(html,"lxml")
                #soup.find("div", {"id": "articlebody"})
                body=(code.find("div", {"id": "bodyContent"}))
                for tag in body.find_all('li'):
                    tag.replaceWith('')
                for tag in body.find_all('img'):
                    tag.replaceWith('')
                for tag in body.find_all('table'):
                    tag.replaceWith('')
                for tag in body.find_all('ol'):
                    tag.replaceWith('')
                text = body.text
            if ("britannica" in url):
                print("BRITANNICA")
                code=bs4.BeautifulSoup(html,"lxml")
                #soup.find("div", {"id": "articlebody"})
                body=(code.find("div", {"class": "grid-sm"}))
                for tag in body.find_all('li'):
                    tag.replaceWith('')
                for tag in body.find_all('img'):
                    tag.replaceWith('')
                for tag in body.find_all('table'):
                    tag.replaceWith('')
                for tag in body.find_all('ol'):
                    tag.replaceWith('')
                for tag in body.find_all("div",{"class":"marketing-content"}):
                    tag.replaceWith('')
                for tag in body.find_all('script'):
                    tag.replaceWith('')
                for tag in body.find_all('cite'):
                    tag.replaceWith('')
                for tag in body.find_all('figure'):
                    tag.replaceWith('')
                text=body.text
            #print(text)
            else:
                text=get_text(html)
            stmnts=sent_tokenize(text)
            d=TFIDF.main(stmnts,cont)
            import operator
            # sorted_d = sorted(d.items(), key=operator.itemgetter(1))
            sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
            connection = pymysql.connect(host='localhost',
                             user='root',
                             password='divya',
                             db='wce',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
            f=open("output.html","r")
            head=f.read()
            try:
                with connection.cursor() as cursor:
                    sql="INSERT INTO `data` VALUES(%s,%s,%s)"
                    cursor.execute(sql,(url,cont,head))
                connection.commit()
            finally:
                connection.close()
        
            i=0
            for x in range(2):
                if i==0:
                    print(sorted_d[x])
                    self.v1.setText(str(sorted_d[x]))
                    i=i+1
                else:
                    print(sorted_d[x])
                    self.v2.setText(str(sorted_d[x]))
                    i = i + 1
                    import webbrowser
                    print(url)
                    webbrowser.open_new_tab(url)
                    webbrowser.open_new("output.html")
                    self.showAlertBox("Alert", "       Operation Done     ")



        except Exception as e:
            print("try1")
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showAlertBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
                        Dialog.setObjectName("Dialog")
                        Dialog.resize(903, 577)
                        Dialog.setStyleSheet("background-color: rgb(85, 170, 255);")
                        self.toolBox = QtWidgets.QToolBox(Dialog)
                        self.toolBox.setGeometry(QtCore.QRect(0, 0, 871, 571))
                        self.toolBox.setObjectName("toolBox")
                        self.page = QtWidgets.QWidget()
                        self.page.setGeometry(QtCore.QRect(0, 0, 871, 517))
                        self.page.setObjectName("page")
                        self.label = QtWidgets.QLabel(self.page)
                        self.label.setGeometry(QtCore.QRect(20, 0, 841, 61))
                        font = QtGui.QFont()
                        font.setFamily("Segoe UI Black")
                        font.setPointSize(30)
                        font.setBold(True)
                        font.setWeight(75)
                        self.label.setFont(font)
                        self.label.setAlignment(QtCore.Qt.AlignCenter)
                        self.label.setObjectName("label")
                        self.label_2 = QtWidgets.QLabel(self.page)
                        self.label_2.setGeometry(QtCore.QRect(120, 140, 191, 51))
                        font = QtGui.QFont()
                        font.setFamily("MV Boli")
                        font.setPointSize(18)
                        self.label_2.setFont(font)
                        self.label_2.setObjectName("label_2")
                        self.label_3 = QtWidgets.QLabel(self.page)
                        self.label_3.setGeometry(QtCore.QRect(110, 250, 201, 41))
                        font = QtGui.QFont()
                        font.setFamily("MV Boli")
                        font.setPointSize(18)
                        self.label_3.setFont(font)
                        self.label_3.setObjectName("label_3")
                        self.url = QtWidgets.QLineEdit(self.page)
                        self.url.setGeometry(QtCore.QRect(330, 140, 471, 51))
                        self.url.setObjectName("url")
                        self.cont = QtWidgets.QLineEdit(self.page)
                        self.cont.setGeometry(QtCore.QRect(330, 250, 471, 51))
                        self.cont.setObjectName("cont")
                        self.pushButton = QtWidgets.QPushButton(self.page)
                        self.pushButton.setGeometry(QtCore.QRect(350, 360, 211, 51))
                        font = QtGui.QFont()
                        font.setFamily("Rockwell")
                        font.setPointSize(19)
                        font.setBold(False)
                        font.setWeight(50)
                        self.pushButton.setFont(font)
                        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
                        self.pushButton.setObjectName("pushButton")
                        self.pushButton.clicked.connect(self.geturl)
                        self.toolBox.addItem(self.page, "")
                        self.page_2 = QtWidgets.QWidget()
                        self.page_2.setGeometry(QtCore.QRect(0, 0, 871, 517))
                        self.page_2.setObjectName("page_2")
                        self.v1= QtWidgets.QLineEdit(self.page_2)
                        self.v1.setGeometry(QtCore.QRect(300, 90, 471, 41))
                        self.v1.setObjectName("v1")
                        self.v2 = QtWidgets.QLineEdit(self.page_2)
                        self.v2.setGeometry(QtCore.QRect(300, 170, 471, 41))
                        self.v2.setObjectName("v2")
                        self.label_4 = QtWidgets.QLabel(self.page_2)
                        self.label_4.setGeometry(QtCore.QRect(100, 90, 141, 31))
                        font = QtGui.QFont()
                        font.setFamily("MV Boli")
                        font.setPointSize(15)
                        self.label_4.setFont(font)
                        self.label_4.setObjectName("label_4")
                        self.label_5 = QtWidgets.QLabel(self.page_2)
                        self.label_5.setGeometry(QtCore.QRect(100, 170, 141, 31))
                        font = QtGui.QFont()
                        font.setFamily("MV Boli")
                        font.setPointSize(14)
                        self.label_5.setFont(font)
                        self.label_5.setObjectName("label_5")
                        self.label_6 = QtWidgets.QLabel(self.page_2)
                        self.label_6.setGeometry(QtCore.QRect(400, 10, 121, 41))
                        font = QtGui.QFont()
                        font.setFamily("Poor Richard")
                        font.setPointSize(21)
                        font.setBold(False)
                        font.setWeight(50)
                        self.label_6.setFont(font)
                        self.label_6.setObjectName("label_6")
                        self.toolBox.addItem(self.page_2, "")

                        self.retranslateUi(Dialog)
                        self.toolBox.setCurrentIndex(0)
                        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "WEB CONTENT EXTRACTION"))
        self.label_2.setText(_translate("Dialog", "Enter URL"))
        self.label_3.setText(_translate("Dialog", "Enter Keyword"))
        self.cont.setPlaceholderText(_translate("Dialog", "Keyword"))
        self.url.setPlaceholderText(_translate("Dialog", "URL"))
        
        self.pushButton.setText(_translate("Dialog", "Get Data"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "Search Data"))
        self.label_4.setText(_translate("Dialog", "Statement 1"))
        self.label_5.setText(_translate("Dialog", "Statement 2"))
        self.label_6.setText(_translate("Dialog", "RESULT"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Result"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = userhome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
