# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userhome.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import urllib.request
from nltk.tokenize import sent_tokenize
from inscriptis import get_text
from PyQt5 import QtCore, QtGui, QtWidgets
from urlaction import URLCheck
from tfidf import TFIDF
import os

class userhome(object):
    def geturl(self):
        try:
            print("url")
            urlvar = self.url.text()
            print("url=", urlvar)

            # self.url.setText("")
            u = URLCheck()
            res = URLCheck.validation(urlvar)
            # print(res)
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
            html = urllib.request.urlopen(url).read().decode('utf-8')
            text = get_text(html)
            print(text)
            stmnts=sent_tokenize(text)
            d=TFIDF.main(stmnts,cont)
            import operator
            # sorted_d = sorted(d.items(), key=operator.itemgetter(1))
            sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

            i=0
            for x in range(2):
                if i==0:
                    print(sorted_d[x])
                    self.v1.setText(str(sorted_d[x]))
                    i=i+1
                else:
                    print(sorted_d[x])
                    self.v2_2.setText(str(sorted_d[x]))
                    i = i + 1
                    os.startfile("output.html")
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
        Dialog.resize(527, 417)
        Dialog.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.toolBox = QtWidgets.QToolBox(Dialog)
        self.toolBox.setGeometry(QtCore.QRect(0, 2, 521, 411))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 521, 357))
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(20, 0, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.url = QtWidgets.QLineEdit(self.page)
        self.url.setGeometry(QtCore.QRect(210, 80, 271, 31))
        self.url.setObjectName("url")
        self.cont = QtWidgets.QLineEdit(self.page)
        self.cont.setGeometry(QtCore.QRect(210, 120, 271, 31))
        self.cont.setObjectName("con")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(190, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        ######################3
        self.pushButton.clicked.connect(self.geturl)
        #################

        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 521, 357))
        self.page_2.setObjectName("page_2")
        self.v1 = QtWidgets.QLineEdit(self.page_2)
        self.v1.setGeometry(QtCore.QRect(180, 60, 311, 41))
        self.v1.setObjectName("v1")
        self.v2 = QtWidgets.QLineEdit(self.page_2)
        self.v2.setGeometry(QtCore.QRect(180, 130, 311, 41))
        self.v2.setObjectName("v2")
         self.v2_2 = QtWidgets.QLineEdit(self.page_5)
        self.v2_2.setGeometry(QtCore.QRect(170, 250, 581, 61))
        self.v2_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.v2_2.setObjectName("v2_2")
       
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(70, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(70, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(220, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(16)
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
