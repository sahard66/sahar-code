from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QCheckBox, QComboBox, QSpinBox, \
    QDoubleSpinBox, QSlider, QDateEdit, QDateTimeEdit, QDial, QLCDNumber, QProgressBar, QRadioButton, QTimeEdit, \
    QListWidget, QMessageBox, QVBoxLayout
# from PyQt5.QtGui import Qt
# from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.x = 850  # מיקום בציר הגובה ביחס למסך
        self.y = 400  # מיקום בציר האורך ביחס למסך
        self.height = 300  # גודל החלון ציר האורך
        self.width = 450  # גודל החלון ציר ההגובה
        self.text = "welcome to X0 game"
        self.initUI()

    def initUI(self):
        self.setGeometry(self.x, self.y, self.height, self.width)
        self.setWindowTitle(self.text)
        self.time = 0
        self.button_is_checked = True
        self.matrix = []
        for i in range(3):
            row = []
            for y in range(3):
                row.append(QtWidgets.QPushButton(self))
            self.matrix.append(row)
        x = 90
        y = 90
        for z in range(3):
            for j in range(3):
                self.matrix[z][j].setGeometry(z * x + 20, j * y + 20, 80, 80)
                self.matrix[z][j].setCheckable(True)
                self.matrix[z][j].clicked.connect(self.set_status)

        self.label_who_win = QLabel("who won ?", self)
        self.label_who_win.setFont(QFont("Time", 13))
        self.label_who_win.move(75, 320)
        self.label_who_win.setStyleSheet("border: 3px solid blue;")
        self.label_who_win.resize(150, 32)

        reset_button = QtWidgets.QPushButton("restart game", self)
        reset_button.move(75, 380)
        reset_button.resize(150, 40)
        reset_button.setFont(QFont("times", 12))
        reset_button.clicked.connect(self.rest_game)

    def rest_game(self):
        self.label_who_win.setText(" ")
        self.button_is_checked = True
        self.time = 0

        for i in range(3):
            for y in range(3):
                self.matrix[i][y].setText(" ")
                self.matrix[i][y].setEnabled(True)
        #print(self.button_is_checked)

    def set_status(self):
        button = self.sender()
        self.time += 1

        if self.button_is_checked == True:
            button.setText("x")
            button.setFont(QFont("times", 20))
            button.setEnabled(False)
            # print(self.button_is_checked) מראה את הסטטסו הנוכיחי TRUE
            self.button_is_checked = False
            # print(button.text)
            # print(self.button_is_checked) מראה את הסטטוס לאחר השינוי FROM TRUE TO FALSE
        elif self.button_is_checked == False:
            button.setText("o")
            button.setFont(QFont("times", 20))
            button.setEnabled(False)
            self.button_is_checked = True

        win = self.who_win()
        if win == True:
            print("good")
            if self.button_is_checked == False:
                self.label_who_win.setText("X won the game")
                self.label_who_win.setFont(QFont("Times", 13))
            elif self.button_is_checked == True:
                self.label_who_win.setText("O won the game")
                self.label_who_win.setFont(QFont("Times", 13))

            for buttons in self.matrix:     # הבעיה בקאע הזה
                for button1 in buttons:
                    button1.setDisabled(True)

        elif self.time == 9:
            self.label_who_win.setText("game tied")

    def who_win(self):
        for i in range(3):
            if self.matrix[0][i].text() == self.matrix[1][i].text() \
                and self.matrix[1][i].text() == self.matrix[2][i].text() \
                    and self.matrix[0][i].text() != "":
                return True
        for i in range(3):
            if self.matrix[i][0].text() == self.matrix[i][1].text() \
                and self.matrix[i][0].text() == self.matrix[i][2].text() \
                    and self.matrix[i][0].text() != "":
                return True

        if self.matrix[0][0].text() == self.matrix[1][1].text() \
                and self.matrix[1][1].text() == self.matrix[2][2].text() \
                and self.matrix[0][0].text() != "":
            return True

        if self.matrix[0][2].text() == self.matrix[1][1].text() \
                and self.matrix[1][1].text() == self.matrix[2][0].text() \
                and self.matrix[0][2].text() != "":
            return True
        else:
            return False


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
