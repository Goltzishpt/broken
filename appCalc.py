# Кнопки %, c, del
# Вывод после операций и равно


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QMainWindow
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont, QIcon


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.unitUI()
        self.save_operation = []

    def unitUI(self):
        # отрисовка программы
        # главное окно
        window = QWidget(self)
        window.setGeometry(0, 0, 330, 460)
        window.setStyleSheet("background-color: rgb(126, 227, 255);")
        self.setGeometry(200, 200, 330, 460)

        # вывод
        self.label = QLabel('0', self)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setGeometry(QRect(0, 0, 310, 60))
        self.label.setStyleSheet("background-color: rgb(223, 140, 255); color: rgb(255, 255, 255); padding: 17px 0 0 0")
        self.label.move(10, 20)
        self.label.setAlignment(Qt.AlignRight)

        # кнопка С
        self.button_c = QPushButton('c', self)
        self.button_c.setFont(font)
        self.button_c.setGeometry(10, 100, 70, 60)
        self.button_c.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка дел
        self.button_del = QPushButton('del', self)
        self.button_del.setFont(font)
        self.button_del.setGeometry(90, 100, 70, 60)
        self.button_del.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка процент
        self.button_percent = QPushButton('%', self)
        self.button_percent.setFont(font)
        self.button_percent.setGeometry(170, 100, 70, 60)
        self.button_percent.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка *
        self.button_star = QPushButton('*', self)
        self.button_star.setFont(font)
        self.button_star.setGeometry(250, 100, 70, 60)
        self.button_star.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 7
        self.button_7 = QPushButton('7', self)
        self.button_7.setFont(font)
        self.button_7.setGeometry(10, 170, 70, 60)
        self.button_7.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 8
        self.button_8 = QPushButton('8', self)
        self.button_8.setFont(font)
        self.button_8.setGeometry(90, 170, 70, 60)
        self.button_8.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 9
        self.button_9 = QPushButton('9', self)
        self.button_9.setFont(font)
        self.button_9.setGeometry(170, 170, 70, 60)
        self.button_9.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка /
        self.button_div = QPushButton('/', self)
        self.button_div.setFont(font)
        self.button_div.setGeometry(250, 170, 70, 60)
        self.button_div.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 4
        self.button_4 = QPushButton('4', self)
        self.button_4.setFont(font)
        self.button_4.setGeometry(10, 240, 70, 60)
        self.button_4.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 5
        self.button_5 = QPushButton('5', self)
        self.button_5.setFont(font)
        self.button_5.setGeometry(90, 240, 70, 60)
        self.button_5.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 6
        self.button_6 = QPushButton('6', self)
        self.button_6.setFont(font)
        self.button_6.setGeometry(170, 240, 70, 60)
        self.button_6.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка -
        self.button_minus = QPushButton('-', self)
        self.button_minus.setFont(font)
        self.button_minus.setGeometry(250, 240, 70, 60)
        self.button_minus.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 1
        self.button_1 = QPushButton('1', self)
        self.button_1.setFont(font)
        self.button_1.setGeometry(10, 310, 70, 60)
        self.button_1.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 2
        self.button_2 = QPushButton('2', self)
        self.button_2.setFont(font)
        self.button_2.setGeometry(90, 310, 70, 60)
        self.button_2.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 3
        self.button_3 = QPushButton('3', self)
        self.button_3.setFont(font)
        self.button_3.setGeometry(170, 310, 70, 60)
        self.button_3.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка +
        self.button_plus = QPushButton('+', self)
        self.button_plus.setFont(font)
        self.button_plus.setGeometry(250, 310, 70, 60)
        self.button_plus.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка 0
        self.button_0 = QPushButton('0', self)
        self.button_0.setFont(font)
        self.button_0.setGeometry(10, 380, 150, 60)
        self.button_0.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка dot
        self.button_dot = QPushButton('.', self)
        self.button_dot.setFont(font)
        self.button_dot.setGeometry(170, 380, 70, 60)
        self.button_dot.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")

        # кнопка =
        self.button_equal = QPushButton('=', self)
        self.button_equal.setFont(font)
        self.button_equal.setGeometry(250, 380, 70, 60)
        self.button_equal.setStyleSheet("background-color: rgb(255, 158, 251); color: rgb(255, 255, 255);")
        self.functions()
        self.show()

    def functions(self):
        # кнопки цифры
        self.button_1.clicked.connect(lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.write_number(self.button_9.text()))
        self.button_0.clicked.connect(lambda: self.write_number(self.button_0.text()))
        self.button_dot.clicked.connect(lambda: self.write_number(self.button_dot.text()))

        # кнопки операторы
        self.button_plus.clicked.connect(lambda: self.func_operation(self.button_plus.text()))
        self.button_minus.clicked.connect(lambda: self.func_operation(self.button_minus.text()))
        self.button_div.clicked.connect(lambda: self.func_operation(self.button_div.text()))
        self.button_star.clicked.connect(lambda: self.func_operation(self.button_star.text()))

        #
        self.button_equal.clicked.connect(lambda: self.func_equal())


    def write_number(self, number):
        if self.label.text() == '0':
            self.label.setText(number)
            self.save_operation.append(number)
        else:
            self.label.setText(self.label.text() + number)
            self.save_operation.append(number)

    def func_operation(self, operation):
        if len(self.save_operation) > 0:
            if self.save_operation[-1] in '0123456789':
                self.save_operation.append(operation)
            else:
                self.save_operation[-1] = operation
        else:
            self.label.setText('0')
        self.label.setText('0')




    def func_del(self):
        # удаление одного символа
        pass

    def func_c(self):
        # обнуление
        pass

    def func_percent(self):
        # функция процента
        pass

    def func_equal(self):
        result = ''
        result += ''.join(self.save_operation)
        print(result[-1], result[-2])
        if result[-1] == '0' or result[-2] == '/':
            self.label.setText('Division by zero!')
        else:
            print(result)
            # проверка на окончание и начало со знака
            if result[0] not in '0123456789':
                result = result[1:]
            if result[-1] not in '0123456789':
                result = result[:-1]
                print(result)
            result_it = eval(result)
            self.label.setText(str(result_it))
            self.save_operation = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    appCalc = Calculator()
    appCalc.setWindowTitle('Calculator')
    app.setWindowIcon(QIcon('imgCalc.png'))
    MainWindow = QMainWindow()
    MainWindow.setWindowIcon(QIcon('imgCalc.png'))
    sys.exit(app.exec_())