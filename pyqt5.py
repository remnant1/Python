# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
#
# class Exam(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.show()
#
#
# app = QApplication(sys.argv)
# w = Exam()
# sys.exit(app.exec_())

#  #############  기본  #######################

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        btn = QPushButton("Push me!", self)                         # 버튼추가
        btn.resize(btn.sizeHint())                                  # 버튼추가
        btn.move(50, 50)                                            # 버튼추가
        btn.clicked.connect(QCoreApplication.instance().quit)       # Core 추가

        self.resize(500, 500)
        self.setWindowTitle("두번째 시간")
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
