from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
import Ui
import Math_operate as MO


class MyMainForm(QMainWindow, Ui.Ui_MainWindow):
    calculator = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 添加数字 0~9 .
        self.pushButton_0.clicked.connect(self.add_number)
        self.pushButton_1.clicked.connect(self.add_number)
        self.pushButton_2.clicked.connect(self.add_number)
        self.pushButton_3.clicked.connect(self.add_number)
        self.pushButton_4.clicked.connect(self.add_number)
        self.pushButton_5.clicked.connect(self.add_number)
        self.pushButton_6.clicked.connect(self.add_number)
        self.pushButton_7.clicked.connect(self.add_number)
        self.pushButton_8.clicked.connect(self.add_number)
        self.pushButton_9.clicked.connect(self.add_number)
        self.pushButton_pi.clicked.connect(self.add_number)
        self.pushButton_e.clicked.connect(self.add_number)
        self.pushButton_dot.clicked.connect(self.add_number)
        # 清除 AC BS
        self.pushButton_AC.clicked.connect(self.clear_textedit)
        self.pushButton_BS.clicked.connect(self.undo_textedit)
        # 添加运算符号 +-*/%^
        self.pushButton_plus.clicked.connect(self.add_number)
        self.pushButton_minus.clicked.connect(self.add_number)
        self.pushButton_times.clicked.connect(self.add_number)
        self.pushButton_divide.clicked.connect(self.add_number)
        self.pushButton_mod.clicked.connect(self.add_number)
        self.pushButton_point.clicked.connect(self.add_number)
        # 添加()
        self.pushButton_left.clicked.connect(self.add_number)
        self.pushButton_right.clicked.connect(self.add_number)
        # calculate
        self.pushButton_equal.clicked.connect(self.calculate)

    # 添加符号
    def add_number(self):
        self.textEdit.insertPlainText(self.sender().text())

    # AC
    def clear_textedit(self):
        self.textEdit.clear()

    # BS
    def undo_textedit(self):
        self.textEdit.textCursor().deletePreviousChar()

    # 计算表达式结果
    def calculate(self):
        expression = self.textEdit.toPlainText()
        answer = MO.Reverse_Polish(expression)
        self.textEdit.append("="+str(answer))
