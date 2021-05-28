import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QFile, QIODevice
from main_window import Ui_MainWindow, QMainWindow


####### this is where we start ########

#### TODO  Regex_engine ######
# This is pretty much done here - just need to create a new interface
# forget about the output, just figure out the inputs now

# look at web design for inspiration
# I don't have to create a working GUI I just need the drop down to be sufficient
# I don't need the templates just yet
# I just need to add more invoices
# make my code more robust and then apply the filters after


class MyApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.open_file)

    def display_results(self):
        # results = "Pie: {}\nCake: {}".format(
        #     self.ui.pie_check.isChecked(), self.ui.cake_check.isChecked())
        # self.ui.results_textedit.setText(results)
        print("print")

    # def open_file(self):
    #     # path = QFileDialog.getOpenFileName(self, )

    #

    def open_file(self):
        # path = QFileDialog.getOpenFileName(self, 'Open a file')

        # So this is a simple version here
        file_path = QFileDialog().getOpenFileName()[0]
        print(file_path)
    # def open_file(self):
    #     path = QFileDialog.getOpenFileName(self, 'Open a file', '',
    #                                        'All Files (*.*)')
    #     if path != ('', ''):
    #         print("File path : " + path[0])

    #     self.ui.inputField.setText(path[0])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()

    sys.exit(app.exec_())


def start():
    aw = Ui_MainWindow()    # Create the main window object, instantiate Ui_MainWindow
    window = QMainWindow()   # Instantiate the QMainWindow class
    # The main window object calls the setupUi method to set the QMainWindow object
    aw.setupUi(window)
    window.show()
    return window


if __name__ == '__main__':

    # Create a QApplication object as the main GUI entry
    App = QApplication(sys.argv)
    window = start()
    sys.exit(App.exec())

# TODO add regex engine
# TODO make the functions work


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     ui_file_name = "mainwindow.ui"
#     ui_file = QFile(ui_file_name)
#     if not ui_file.open(QIODevice.ReadOnly):
#         print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
#         sys.exit(-1)
#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     ui_file.close()
#     if not window:
#         print(loader.errorString())
#         sys.exit(-1)
#     window.show()

#     sys.exit(app.exec_())

# # I can use the builder to create the main window.
# # output terminal to GUI
