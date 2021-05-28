from pdfparser import parse_pages
import sys

from pdftotext import pdf_to_text
from PyQt6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget, QLineEdit, QPushButton, QFileDialog, QErrorMessage, \
    QComboBox, QTabWidget

from PyQt6.QtCore import pyqtSlot

from mann_hummel import extract_mann
from pdfparser import parse_pages
from electrolux import extract_electro

# select template
# TODO create template - dynamically add option to combobox - or create a list of templates to
# select from

# TODO select file - text
# TODO select template - text

# add combo box here


# def parse_pdf(number_of_pages, pdf):
#     full_text = ''

#     for i in range(number_of_pages):
#         page = pdf.pages[i].extract_text()
#         full_text += filter_invoice(page)

#     matched_items = re.findall(new_item, full_text)
#     return matched_items


# this is the GUI I made wihtout the use of the QT Designer.
# QT Designer hasn't helped me much in the way of making anything useful yet.

class layout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Andromeda')
        self.setFixedSize(300, 160)
        # self.setWindowIcon('maps.ico')
        # self.resize()  # width, height

        # so we define the layout and then set the layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # self.tabs = QTabWidget()
        # self.tab1 = QWidget()
        # self.tab2 = QWidget()

        self.inputField = QLineEdit()

        button = QPushButton('Browse')
        button.clicked.connect(self.open_file)

        # self.tabs.addTab(self.tab1, "Tab 1")
        # self.tabs.addTab(self.tab2, "Tab 2")

        # TODO add the items to the template dynamically - choose
        self.comboBox = QComboBox()
        self.comboBox.addItem('No Selection')
        self.comboBox.addItem('Mann + Hummel')
        self.comboBox.addItem('ElectroLux')

        convert_button = QPushButton('Convert to Text')
        convert_button.clicked.connect(self.extract)

        # self.output = QTextEdit()

        # self.table_widget = TabWidget(self)
        # self.setCentralWidget(self.table_widget)

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.comboBox)
        layout.addWidget(convert_button)

    def open_file(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])

        self.inputField.setText(path[0])

# select the template that we want
    def extract(self):
        try:
            if str(self.comboBox.currentText()) == 'Mann + Hummel':
                # add the old code here

                print('Mann + Hummel')
                # pass the file path here.

                parse_pages(self.inputField.text())

                # matched_items = parse_pdf(self.inputField.text())
                # from other pdf

            elif str(self.comboBox.currentText()) == 'ElectroLux':

                print('ElectroLux')
                extract_electro(self.inputField.text())
            else:
                pdf_to_text(self.inputField.text())
        except Exception as e:
            print(e)
            # error_dialog = QErrorMessage()
            # error_dialog.showMessage('Oh no!')
# add another button first


# class TabWidget():
#     def __init__(self, parent):
#         super(QWidget, self).__init__(parent)
#         self.layout = QVBoxLayout(self)

#         # Initialize tab screen
#         # self.tabs = QTabWidget()
#         # self.tab1 = QWidget()
#         # self.tab2 = QWidget()
#         self.tabs.resize(300, 200)

#         # Add tabs
#         self.tabs.addTab(self.tab1, "Tab 1")
#         self.tabs.addTab(self.tab2, "Tab 2")

#         # Create first tab
#         self.tab1.layout = QVBoxLayout(self)
#         self.pushButton1 = QPushButton("PyQt5 button")
#         self.tab1.layout.addWidget(self.pushButton1)
#         self.tab1.setLayout(self.tab1.layout)

#         # Add tabs to widget
#         self.layout.addWidget(self.tabs)
#         self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


# pistachio green

# pass the file path to a variable
# add the path to the text box
# the following sequence allows me to show the application
app = QApplication(sys.argv)
# app.setStyleSheet(
#     '''


#     '''

# )
# # apply_stylesheet(app, theme='dark_teal.xml')

window = layout()
window.show()

app.exec()
