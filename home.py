# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'F:\CT\uis\home.ui'
# Created by: PyQt5 UI code generator 5.11.3
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from userloginaction import UserLoginCheck
from userhome import userhome

from PyQt5 import QtCore, QtGui, QtWidgets

class home(object):
	def userlogin(self):
		try:
			print("adminlogin")
			uidvar = self.uid.text()
			pwdvar = self.pwd.text()
			self.uid.setText("")
			self.pwd.setText("")
			al = UserLoginCheck()
			res = al.datacheck(uidvar, pwdvar)
			if res:
				self.showAlertBox("Alert", "Fill the Fields")
			elif UserLoginCheck.logincheck(uidvar, pwdvar):
				self.u = QtWidgets.QDialog()
				self.ui = userhome()
				self.ui.setupUi(self.u)
				self.u.show()
				self.dialog.hide()
			else:
				self.showAlertBox("Login Alert", "Login Fail")

		except Exception as e:
				print(e.args[0])
				tb = sys.exc_info()[2]
				print(tb.tb_lineno)

	#
	##Alert Winwow
	#
	def showAlertBox(self, title, message):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Warning)
		msgBox.setWindowTitle(title)
		msgBox.setText(message)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()

	def setupUi(self, MainWindow):
			MainWindow.setObjectName("MainWindow")
			MainWindow.resize(785, 574)
			MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
			self.centralwidget = QtWidgets.QWidget(MainWindow)
			self.centralwidget.setObjectName("centralwidget")
			
			self.label = QtWidgets.QLabel(self.centralwidget)
			self.label.setGeometry(QtCore.QRect(10, 6, 771, 61))
			font = QtGui.QFont()
			font.setFamily("MV Boli")
			font.setPointSize(30)
			self.label.setFont(font)
			self.label.setStyleSheet("color: rgb(85, 85, 255);")
			self.label.setAlignment(QtCore.Qt.AlignCenter)
			self.label.setObjectName("label")
			
			self.label_2 = QtWidgets.QLabel(self.centralwidget)
			self.label_2.setGeometry(QtCore.QRect(190, 300, 151, 21))
			font = QtGui.QFont()
			font.setPointSize(15)
			self.label_2.setFont(font)
			self.label_2.setStyleSheet("color: rgb(85, 170, 255);")
			self.label_2.setObjectName("label_2")
			
			self.label_3 = QtWidgets.QLabel(self.centralwidget)
			self.label_3.setGeometry(QtCore.QRect(190, 370, 171, 20))
			font = QtGui.QFont()
			font.setPointSize(15)
			self.label_3.setFont(font)
			self.label_3.setStyleSheet("color: rgb(85, 170, 255);")
			self.label_3.setObjectName("label_3")
			
			self.uid = QtWidgets.QLineEdit(self.centralwidget)
			self.uid.setGeometry(QtCore.QRect(400, 290, 261, 31))
			font = QtGui.QFont()
			font.setPointSize(15)
			self.uid.setFont(font)
			self.uid.setStyleSheet("color: rgb(255, 255, 255);")
			self.uid.setObjectName("uid")
			
			self.pwd = QtWidgets.QLineEdit(self.centralwidget)
			self.pwd.setGeometry(QtCore.QRect(400, 360, 261, 31))
			font = QtGui.QFont()
			font.setPointSize(15)
			self.pwd.setFont(font)
			self.pwd.setStyleSheet("color: rgb(255, 255, 255);")
			self.pwd.setObjectName("pwd")
			self.pwd.setText("")
			self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
			
			self.ulogin = QtWidgets.QPushButton(self.centralwidget)
			self.ulogin.setGeometry(QtCore.QRect(330, 450, 161, 41))
			font = QtGui.QFont()
			font.setPointSize(16)
			self.ulogin.setFont(font)
			self.ulogin.setStyleSheet("background-color: rgb(85, 170, 255);")
			self.ulogin.setObjectName("ulogin")
			self.ulogin.clicked.connect(self.userlogin)

			self.label_4 = QtWidgets.QLabel(self.centralwidget)
			self.label_4.setGeometry(QtCore.QRect(330, 90, 131, 161))
			self.label_4.setMaximumSize(QtCore.QSize(16777215, 171))
			self.label_4.setText("")
			self.label_4.setPixmap(QtGui.QPixmap("../icon.png"))
			self.label_4.setObjectName("label_4")
			MainWindow.setCentralWidget(self.centralwidget)
			self.statusbar = QtWidgets.QStatusBar(MainWindow)
			self.statusbar.setObjectName("statusbar")
			MainWindow.setStatusBar(self.statusbar)

			self.retranslateUi(MainWindow)
			QtCore.QMetaObject.connectSlotsByName(MainWindow)
	def retranslateUi(self, MainWindow):
				_translate = QtCore.QCoreApplication.translate
				_translate = QtCore.QCoreApplication.translate
				MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
				self.label.setText(_translate("MainWindow", "WEB CONTENT EXTRACTOR"))
				self.label_2.setText(_translate("MainWindow", "Enter User Id"))
				self.label_3.setText(_translate("MainWindow", "Enter Password"))
				self.ulogin.setText(_translate("MainWindow", "Login"))
				self.uid.setPlaceholderText(_translate("MainWindow", "Enter UserID"))
				self.pwd.setPlaceholderText(_translate("MainWindow", "Enter Password"))

if __name__ == "__main__":
					import sys
					app = QtWidgets.QApplication(sys.argv)
					MainWindow = QtWidgets.QMainWindow()
					ui = home()
					ui.setupUi(MainWindow)
					MainWindow.show()
					sys.exit(app.exec_())

