import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
    app = QApplication(sys.argv)
    widget = QWidget()

    button1 = QPushButton(widget)
    button1.setText("Secure Password")
    button1.move(64, 32)
    button1.clicked.connect(button1_clicked)


    button2 = QPushButton(widget)
    button2.setText("Insane Secure Password")
    button2.move(64, 64)
    button2.clicked.connect(button2_clicked)

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("Generate Secure Password")
    widget.show()
    sys.exit(app.exec_())


def button1_clicked():
    import random
    import string

    # A function do shuffle all the characters of a string
    def shuffle(string):
        tempList = list(string)
        random.shuffle(tempList)
        return ''.join(tempList)

    pass1var = string.ascii_letters
    password = shuffle(pass1var)

    msgBox = QMessageBox()
    msgBox.setText(password)
    msgBox.exec()

def button2_clicked():
    import random
    import string

    # A function do shuffle all the characters of a string
    def shuffle(string):
        tempList = list(string)
        random.shuffle(tempList)
        return ''.join(tempList)

    pass2var1 = string.ascii_letters
    pass2var2 = string.ascii_letters
    password = shuffle(pass2var1 + pass2var2)

    msgBox = QMessageBox()
    msgBox.setText(password)
    msgBox.exec()

if __name__ == '__main__':
    window()