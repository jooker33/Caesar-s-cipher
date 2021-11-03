# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QInputDialog
import datetime as dt

#Lets set basic veriables that we need 
Alph_Lat=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']*2
Alph_Cyr=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']*2
key=0

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Перед началом работы, обязательно пропишите ниже ваш индвидуальный путь к файлу истории операций
		self.history_way='C:/Users/Nikkt/PycharmProjects/Caesar_qt5/QT/history_file.txt'

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!		
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(697, 770)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
		self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 701, 801))
		self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
		self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.Butt_decr = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
		self.Butt_decr.setObjectName("Butt_decr")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.Text_1_enc = QtWidgets.QPlainTextEdit(self.tab)
		self.Text_1_enc.setGeometry(QtCore.QRect(0, 40, 691, 271))
		self.Text_1_enc.setObjectName("Text_1_enc")
		self.Text_2_enc = QtWidgets.QPlainTextEdit(self.tab)
		self.Text_2_enc.setGeometry(QtCore.QRect(0, 370, 691, 271))
		self.Text_2_enc.setObjectName("Text_2_enc")
		self.Butt_enc = QtWidgets.QPushButton(self.tab)
		self.Butt_enc.setGeometry(QtCore.QRect(270, 660, 171, 61))
		self.Butt_enc.setObjectName("Butt_enc")
		self.label_key = QtWidgets.QLabel(self.tab)
		self.label_key.setGeometry(QtCore.QRect(30, 670, 120, 41))
		self.label_key.setObjectName("label_key")
		self.doubleSpinBox_1_KEY = QtWidgets.QDoubleSpinBox(self.tab)
		self.doubleSpinBox_1_KEY.setGeometry(QtCore.QRect(160, 680, 62, 22))
		self.doubleSpinBox_1_KEY.setDecimals(0)
		self.doubleSpinBox_1_KEY.setMinimum(-100.0)
		self.doubleSpinBox_1_KEY.setMaximum(100.0)
		self.doubleSpinBox_1_KEY.setObjectName("doubleSpinBox_1_KEY")
		self.label = QtWidgets.QLabel(self.tab)
		self.label.setGeometry(QtCore.QRect(10, 10, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.tab)
		self.label_2.setGeometry(QtCore.QRect(10, 330, 211, 35))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.Butt_decr.addTab(self.tab, "")
		self.tab_2_decryption = QtWidgets.QWidget()
		self.tab_2_decryption.setObjectName("tab_2_decryption")
		self.Text_1_decr = QtWidgets.QPlainTextEdit(self.tab_2_decryption)
		self.Text_1_decr.setGeometry(QtCore.QRect(0, 40, 691, 271))
		self.Text_1_decr.setObjectName("Text_1_decr")
		self.Text_2_decr = QtWidgets.QPlainTextEdit(self.tab_2_decryption)
		self.Text_2_decr.setGeometry(QtCore.QRect(0, 370, 691, 271))
		self.Text_2_decr.setObjectName("Text_2_decr")
		self.pushButton_2 = QtWidgets.QPushButton(self.tab_2_decryption)
		self.pushButton_2.setGeometry(QtCore.QRect(270, 660, 171, 61))
		self.pushButton_2.setObjectName("pushButton_2")
		self.label_2_key = QtWidgets.QLabel(self.tab_2_decryption)
		self.label_2_key.setGeometry(QtCore.QRect(30, 670, 120, 41))
		self.label_2_key.setObjectName("label_2_key")
		self.doubleSpinBox_2_KEY = QtWidgets.QDoubleSpinBox(self.tab_2_decryption)
		self.doubleSpinBox_2_KEY.setGeometry(QtCore.QRect(160, 680, 62, 22))
		self.doubleSpinBox_2_KEY.setDecimals(0)
		self.doubleSpinBox_2_KEY.setMinimum(-100.0)
		self.doubleSpinBox_2_KEY.setMaximum(100.0)
		self.doubleSpinBox_2_KEY.setObjectName("doubleSpinBox_2_KEY")
		self.label_4 = QtWidgets.QLabel(self.tab_2_decryption)
		self.label_4.setGeometry(QtCore.QRect(10, 330, 250, 35))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_3 = QtWidgets.QLabel(self.tab_2_decryption)
		self.label_3.setGeometry(QtCore.QRect(10, 10, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.Butt_decr.addTab(self.tab_2_decryption, "")
		self.tab_3_history = QtWidgets.QWidget()
		self.tab_3_history.setObjectName("tab_3_history")
		self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3_history)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 691, 771))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.plainTextEdit_5_history = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
		self.plainTextEdit_5_history.setObjectName("plainTextEdit_5_history")

		self.plainTextEdit_5_history.setGeometry(100,0,691,771)

		self.verticalLayout.addWidget(self.plainTextEdit_5_history)
		self.Butt_decr.addTab(self.tab_3_history, "")
		self.verticalLayout_3.addWidget(self.Butt_decr)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.Butt_decr.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		self.history_file=open(self.history_way,'r')
		self.plainTextEdit_5_history.setPlainText(self.history_file.read())
#Обработаем клики ниже
		self.Butt_enc.clicked.connect(self.lets_start_to_encrypt)

		self.pushButton_2.clicked.connect(self.lets_start_to_decrypt)



	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Цезарь Код"))
		
		self.Butt_enc.setText(_translate("MainWindow", "Шифровать"))
		self.label_key.setText(_translate("MainWindow", "Ключ шифрования"))
		self.label.setText(_translate("MainWindow", "Ваш текст: "))
		self.label_2.setText(_translate("MainWindow", "Шифровка:"))
		self.Butt_decr.setTabText(self.Butt_decr.indexOf(self.tab), _translate("MainWindow", "Шифратор"))
		
		self.pushButton_2.setText(_translate("MainWindow", "Дешифровать"))
		self.label_2_key.setText(_translate("MainWindow", "Ключ шифрования"))
		self.label_4.setText(_translate("MainWindow", "Расшифровка: "))
		self.label_3.setText(_translate("MainWindow", "Шифровка:"))
		self.Butt_decr.setTabText(self.Butt_decr.indexOf(self.tab_2_decryption), _translate("MainWindow", "Дешифратор"))
		self.Butt_decr.setTabText(self.Butt_decr.indexOf(self.tab_3_history), _translate("MainWindow", "История"))








	def translate_to(self,str_input,key):
		str_output=''
#		if str_input[0].upper() in Alph_Lat:
		for i in str_input:
			if i.upper() not in Alph_Lat:
				str_output+=i
			else:
				real_index=Alph_Lat.index(i.upper())
				new_index= Alph_Lat.index(i.upper()) + key%26
				# Получили индекс буквы i в списке букв алфавита и прибавили к нему ключ
				str_output+=Alph_Lat[new_index]

#Убрав комментариии в этой функции и поправить, можно подключить Русский язык для шифрования с простейшим рапознаванием языка по первой букве фразы.
#		elif str_input[0].upper() in Alph_Cyr:
#			for i in str_input:
#
#				if i.upper() not in Alph_Cyr:
#					str_output+=i
#
#				else:
#					real_index=Alph_Cyr.index(i.upper())
#					new_index= Alph_Cyr.index(i.upper()) + key%33
#					# Получили индекс буквы i в списке букв алфавита и прибавили к нему ключ
#					str_output+=Alph_Cyr[new_index]
#					
#		else:
#			print('Язык не распознан или первыйы элемент не буква')


		
		self.Text_2_enc.setPlainText(str_output.lower())
		self.plainTextEdit_5_history.setPlainText(self.plainTextEdit_5_history.toPlainText() + 'Случай Зашифровки '+' | '+ self.give_me_time() +'\n'+str_input+'\n'+'Зашифровано в '+'\n'+str_output.lower()+'\n' +'с Ключом: '+str(key)+'\n'*3)
		self.history_file=open(self.history_way,'a')
		self.history_file.write('Случай Зашифровки '+' | '+ self.give_me_time()+'\n'+str_input+'\n'+'Зашифровано в '+'\n'+str_output.lower()+'\n' +'с Ключом: '+str(key)+'\n'*3)
		self.history_file.close()

	def translate_from(self,str_input,key):

		str_output=''
#		if str_input[0].upper() in Alph_Lat:
		for i in str_input:
			if i.upper() not in Alph_Lat:
				str_output+=i
			else:
				real_index=Alph_Lat.index(i.upper())
				new_index= Alph_Lat.index(i.upper()) - key%26
				# Получили индекс буквы i в списке букв алфавита и прибавили к нему ключ
				str_output+=Alph_Lat[new_index]
#Убрав комментариии в этой функции и поправив отступы, можно подключить Русский язык для ДеШифрования с простейшим рапознаванием языка по первой букве фразы.
#		elif str_input[0].upper() in Alph_Cyr:
#			for i in str_input:
#
#				if i.upper() not in Alph_Cyr:
#					str_output+=i
#
#				else:
#					real_index=Alph_Cyr.index(i.upper())
#					new_index= Alph_Cyr.index(i.upper()) - key%33
#					# Получили индекс буквы i в списке букв алфавита и прибавили к нему ключ
#					str_output+=Alph_Cyr[new_index]
#				
#		else: 
#			print('Язык не распознан или первыйы элемент не буква')

		
		self.Text_2_decr.setPlainText(str_output.lower())
		self.plainTextEdit_5_history.setPlainText(self.plainTextEdit_5_history.toPlainText() + 'Случай Дешифровки '+' | '+ self.give_me_time() +'\n'+str_input+'\n'+'Дешифровано в: '+'\n'+str_output.lower()+'\n' +'с Ключом: '+str(key)+'\n'*3)

		self.history_file=open(self.history_way,'a')
		self.history_file.write('Случай Дешифровки '+' | '+ self.give_me_time()+'\n'+str_input+'\n'+'Дешифровано в: '+'\n'+str_output.lower()+'\n' +'с Ключом: '+str(key)+'\n'*3)
		self.history_file.close()

	def lets_start_to_encrypt(self):
		key=int(self.doubleSpinBox_1_KEY.text())
		str_input=self.Text_1_enc.toPlainText()
		
		self.translate_to(str_input,key)

	def lets_start_to_decrypt(self):
		key=int(self.doubleSpinBox_2_KEY.text())
		str_input=self.Text_1_decr.toPlainText()
		self.translate_from(str_input,key)

	def give_me_time(self):
		self.current_time=dt.datetime.now().strftime('%d of %B %Y | %H:%M_%S')
		return self.current_time

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
