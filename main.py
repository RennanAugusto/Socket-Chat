# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
import emoji
import socket
import threading
import time
import datetime
import sys

#   Definição da host
host = 'localhost'
port = 8080

#   Criação do socket TCP/IP
try:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((host, port))
except:
    print('Cara não deu pra conectar n')
    
class Ui_MainWindow(object):

    def __init__(self):
        thread1 = threading.Thread(target = self.get_message)
        thread1.start()

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 594)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 0, 771, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 769, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 771, 401))
        self.listWidget.setObjectName("listWidget")

        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 771, 401))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 769, 399))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea_2.raise_()

        self.listWidget.raise_()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.btnMsg = QtWidgets.QPushButton(self.centralwidget) 
        self.btnMsg.setGeometry(QtCore.QRect(690, 480, 91, 71))
        self.btnMsg.setObjectName("btnMsg")
        self.btnMsg.setStyleSheet("background-color: rgb( 200, 200, 200 ); border-image: url(:/src/enviar.png);")
        rMyIcon = QtGui.QPixmap("src/enviar.ico")
        self.btnMsg.setIcon(QtGui.QIcon(rMyIcon))

        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(10, 450, 191, 21))
        self.name.setObjectName("textEdit")

        self.messageText = QtWidgets.QTextEdit(self.centralwidget)
        self.messageText.setGeometry(QtCore.QRect(10, 480, 491, 71))
        self.messageText.setObjectName("messageText")

        self.emoticon_1 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_1.setGeometry(QtCore.QRect(520, 480, 31, 31))
        self.emoticon_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_1.setObjectName("emoticon_1")

        self.emoticon_2 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_2.setGeometry(QtCore.QRect(560, 480, 31, 31))
        self.emoticon_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_2.setObjectName("emoticon_2")

        self.emoticon_3 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_3.setGeometry(QtCore.QRect(600, 480, 31, 31))
        self.emoticon_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_3.setObjectName("emoticon_3")

        self.emoticon_4 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_4.setGeometry(QtCore.QRect(640, 480, 31, 31))
        self.emoticon_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_4.setObjectName("emoticon_4")

        self.emoticon_5 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_5.setGeometry(QtCore.QRect(520, 520, 31, 31))
        self.emoticon_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_5.setObjectName("emoticon_5")

        self.emoticon_6 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_6.setGeometry(QtCore.QRect(560, 520, 31, 31))
        self.emoticon_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_6.setObjectName("emoticon_6")

        self.emoticon_7 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_7.setGeometry(QtCore.QRect(600, 520, 31, 31))
        self.emoticon_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_7.setObjectName("emoticon_7")
        
        self.emoticon_8 = QtWidgets.QPushButton(self.centralwidget)
        self.emoticon_8.setGeometry(QtCore.QRect(640, 520, 31, 31))
        self.emoticon_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.emoticon_8.setObjectName("emoticon_8")

        self.btnLogar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogar.setGeometry(QtCore.QRect(210, 450, 75, 21))
        self.btnLogar.setObjectName("btnLogar")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #mouselisteners
        self.btnMsg.clicked.connect(self.send_message)
        self.btnLogar.clicked.connect(self.logar)
        self.emoticon_1.clicked.connect(self.get_emote1)
        self.emoticon_2.clicked.connect(self.get_emote2)
        self.emoticon_3.clicked.connect(self.get_emote3)
        self.emoticon_4.clicked.connect(self.get_emote4)
        self.emoticon_5.clicked.connect(self.get_emote5)
        self.emoticon_6.clicked.connect(self.get_emote6)
        self.emoticon_7.clicked.connect(self.get_emote7)
        self.emoticon_8.clicked.connect(self.get_emote8)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnMsg.setText(_translate("MainWindow", 'Enviar'))
        self.emoticon_1.setText(_translate("MainWindow", emoji.emojize('\U0001F44D')))
        self.emoticon_2.setText(_translate("MainWindow", emoji.emojize('\U0001F64F')))
        self.emoticon_3.setText(_translate("MainWindow", emoji.emojize('\U0001F44B')))
        self.emoticon_4.setText(_translate("MainWindow", emoji.emojize('\U0001F4A5')))
        self.emoticon_5.setText(_translate("MainWindow", emoji.emojize('\U0001F923')))
        self.emoticon_6.setText(_translate("MainWindow", emoji.emojize('\U0001F61B')))	
        self.emoticon_7.setText(_translate("MainWindow", emoji.emojize('\U0001F4A9')))
        self.emoticon_8.setText(_translate("MainWindow", emoji.emojize('\U0001F637')))
        self.btnLogar.setText(_translate("MainWindow", "Logar"))

    def get_emote1(self):
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F44D ')

    def get_emote2(self):
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F64F ')

    def get_emote3(self):
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F44B ')

    def get_emote4(self):    
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F4A5 ')

    def get_emote5(self):    
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F923 ')

    def get_emote6(self):   
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F61B ')

    def get_emote7(self):
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F4A9 ')

    def get_emote8(self):        
        self.messageText.setPlainText(self.messageText.toPlainText() + '\U0001F637 ')

    def send_message(self):
        if self.name.text == '':
            return
            
        res = self.get_date() +' ' + self.name.text() + ' : ' + self.messageText.toPlainText()
        item = emoji.emojize(res)
        tcp.send(res.encode('utf-8'))
        self.listWidget.addItem(item)
        self.messageText.setPlainText('') 

    def get_date(self):
       data_e_hora_atuais = datetime.datetime.now()
       data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
       return data_e_hora_em_texto

    def get_message(self):
        while True:
           data = tcp.recv(1024).decode('utf-8')
           self.listWidget.addItem(emoji.emojize(data))      

    def logar(self):
        name = '------' + str(self.name.text()) + ' Entrou' + '------'
        tcp.send(name.encode('utf-8'))
        self.listWidget.addItem(name)
        self.name.setReadOnly(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
