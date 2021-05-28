
import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QComboBox, QVBoxLayout, \
    QWidget, QLineEdit, QPushButton, QFileDialog, QErrorMessage, \
    QComboBox, QTabWidget, QMainWindow, QTextEdit, QStatusBar

from PyQt6.QtCore import QCoreApplication, QMetaObject, QRect, pyqtSlot, QObject

from Extraction.mann_hummel import extract_mann
# from pdfparser import parse_pages
from Extraction.electrolux import extract_electro
from Extraction.pdf_to_text import pdf_to_text

# I'm starting with this integrated terminal that I'm making
# It's part of an idea but it'll be the next iteration.
# version 2.

# def setupui


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        super().__init__()
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 713)
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 610, 121, 21))

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 610, 331, 21))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(540, 640, 121, 21))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 20, 771, 571))
        self.textEdit.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
                                    "font: 10pt \"Consolas\";\n"
                                    "color: rgb(170, 255, 127);")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.addItem('No Selection')

        # only extras I added
        self.comboBox.addItem('Mann + Hummel')
        self.comboBox.addItem('ElectroLux')
        self.comboBox.setGeometry(QRect(200, 640, 331, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.actionImport.setText(
            QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExit.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Browse", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "MainWindow", u"Convert to Text", None))
        # retranslateUi

    # def open_file(self):
    #     print("testing")

    # def extract(self):
    #     try:
    #         if str(self.comboBox.currentText()) == 'Mann + Hummel':
    #             # add the old code here

    #             print('Mann + Hummel')
    #             # pass the file path here.

    #             #### TODO PARSE PAGES HERE? ######
    #             # parse_pages(self.inputField.text())

    #             # matched_items = parse_pdf(self.inputField.text())
    #             # from other pdf

    #         elif str(self.comboBox.currentText()) == 'ElectroLux':

    #             print('ElectroLux')
    #             # extract_electro(self.inputField.text())
    #         else:
    #             pdf_to_text(self.inputField.text())
    #     except Exception as e:
    #         print(e)
