import sys
from points import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import datetime as dt
from PyQt5.QtWidgets import QApplication, QMainWindow


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.btn.clicked.connect(self.run)
        self.date = [[self.day1, self.month1, self.year1, self.age1], [self.day2, self.month2, self.year2, self.age2],
                     [self.day3, self.month3, self.year3, self.age3], [self.day4, self.month4, self.year4, self.age4]]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == 16777220:
            self.run()

    def run(self):
        sp = []
        if self.btn1.checkState():
            sp.append(1)
        if self.btn2.checkState():
            sp.append(2)
        if self.btn3.checkState():
            sp.append(3)
        if self.btn4.checkState():
            sp.append(4)
        if len(sp) != 2:
            self.error.setText('Необходимо выбрать 2 даты')
            return
        d1 = self.date[sp[0] - 1][0].value()
        m1 = self.date[sp[0] - 1][1].value()
        y1 = self.date[sp[0] - 1][2].text()
        if check(d1, m1, y1) == -1:
            self.error.setText(f'Даты номер {sp[0]} не существует')
            return 
        y1 = int(y1)
        d2 = self.date[sp[1] - 1][0].value()
        m2 = self.date[sp[1] - 1][1].value()
        y2 = self.date[sp[1] - 1][2].text()
        if check(d2, m2, y2) == -1:
            self.error.setText(f'Даты номер {sp[1]} не существует')
            return 
        y2 = int(y2)
        t = check_time(d1, m1, y1, d2, m2, y2)
        if (t == -1 and sp[0] != 2) or (t != -1 and sp[0] == 2):
            self.error.setText(f'Неправильный порядок дат')
            return
        try:
            date1 = add_date(y1, m1, d1)
        except:
            self.error.setText(f'Даты номер {sp[0]} не существует')
            return
        try:
            date2 = add_date(y2, m2, d2)
        except:
            self.error.setText(f'Даты номер {sp[1]} не существует')
            return
        try:
            ans = calculate(sp[0], date1, sp[1], date2)
        except:
            self.error.setText('Упс...Что-то пошло не так')
            return
        for i in range(4):
            self.date[i][0].setValue(ans[i][1].day)
            self.date[i][1].setValue(ans[i][1].month)
            self.date[i][2].setText(str(ans[i][1].year + 9800 * ans[i][0]))
            d, m, y = age(ans[0], ans[i])
            self.date[i][3].setText(f'{y} л. {m} м. {d} дн.')
        self.error.setText('')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
