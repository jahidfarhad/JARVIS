# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisGUI(object):
    def setupUi(self, jarvisGUI):
        jarvisGUI.setObjectName("jarvisGUI")
        jarvisGUI.resize(720, 401)
        self.centralwidget = QtWidgets.QWidget(jarvisGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -100, 801, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/Programming/Python/Projects/JARVIS/Interface/pwuXrz.gif"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 340, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 370, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background:transparent;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(240, 10, 256, 31))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        jarvisGUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisGUI)
        QtCore.QMetaObject.connectSlotsByName(jarvisGUI)

    def retranslateUi(self, jarvisGUI):
        _translate = QtCore.QCoreApplication.translate
        jarvisGUI.setWindowTitle(_translate("jarvisGUI", "MainWindow"))
        self.pushButton.setText(_translate("jarvisGUI", "RUN"))
        self.pushButton_2.setText(_translate("jarvisGUI", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisGUI = QtWidgets.QMainWindow()
    ui = Ui_jarvisGUI()
    ui.setupUi(jarvisGUI)
    jarvisGUI.show()
    sys.exit(app.exec_())
