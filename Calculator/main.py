# This Python file uses the following encoding: utf-8
import sys
import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore


if __name__ == "__main__":
    # 适配2k高分辨率屏幕
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MainWindow.MyMainForm()
    myWin.show()
    sys.exit(app.exec_())