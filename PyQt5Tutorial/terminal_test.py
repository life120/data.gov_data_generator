# https://zetcode.com/gui/pyqt5/datetime/
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QIcon
# Retrieves current Date and creates a QDate object
nowDate = QDate.currentDate()
# Prints out current data in ISO e.g. 2021-05-22
print(nowDate.toString(Qt.ISODate))
#  Prints out current date in long term Saturday, 22 May 2021
print(nowDate.toString(Qt.DefaultLocaleLongDate))
# Retrieves current Date and Time
datetime = QDateTime.currentDateTime()
# Prints retrieved current date time in a format e.g. Sat May 22 10:43:55 2021
print(datetime.toString())
# retrieves current time
time = QTime.currentTime()
# Prints retrieved
print(time.toString())
# Create a date QDate(y,m,d) object
xmas1 = QDate(2019, 12, 24)
# Find the difference in terms of days and returns an integer
dayspassed = xmas1.daysTo(nowDate)
print(f'{dayspassed} days have passed since Christmas 2019')
# Add days, months and years to a datetime
print(f'Current Date: {datetime.toString(Qt.ISODate)}')
print(f'Adding 12 days: {datetime.addDays(12).toString(Qt.ISODate)}')
print(f'Adding 3 months: {datetime.addMonths(3).toString(Qt.ISODate)}')
print(f'Adding 12 years: {datetime.addYears(9).toString(Qt.ISODate)}')

#### first program ####


class main_window(QWidget):
    def __init__(self):
        # initialise the subclass as well
        super().__init__()
        self.initUI()

    def initUI(self):
        # for setGeometry, first 2 params is the location of where the window will be, the next 2 params is the width and height respectively (Combines resize and move in one)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Main Window')
        # self.resize(250,150)
        # self.move(150,150) #(width, height)
        btn = QPushButton('Close', self)
        btn.move(0, 180)
        btn.resize(50, 25)
        btn.clicked.connect(QApplication.instance().quit)
        # create a tooltip float
        btn.setToolTip('This is a button')

        self.setWindowIcon(QIcon('WaterMask.png'))
        self.show()


def main():
    # sys.argv parameter is a list of arguments from a command line
    app = QApplication(sys.argv)
    # # create a QWidget instance
    # w = QWidget()
    # # resize the QWidget window instance
    # w.resize(250, 150)
    # # move the QWidget from the top left
    # w.move(150, 150)
    # # change the title of the widget
    # w.setWindowTitle('Simple')
    # # show the window and puts it into a main loop
    # w.show()
    window = main_window()
    # The sys.exit() method ensures a clean exit
    sys.exit(app.exec_())


main()
