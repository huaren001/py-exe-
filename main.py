# -*- coding: utf-8 -*-
"""
导入模块
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import PyInstaller.__main__

class Ui_MainWindow(object):       # 定义一个名为Ui_MainWindow的类
    def setupUi(self, MainWindow):       # 定义setupUi函数，用于设置UI界面
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(888, 479)
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(137, 245, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 100, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 170, 551, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(137, 245, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 240, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """
        将按钮的点击事件与下面另一个指定的函数连接起来
        """
        self.pushButton.clicked.connect(self.open_filr)
        self.pushButton_3.clicked.connect(self.convert_to_exe)
        self.pushButton_2.clicked.connect(self.set_icon_path)

    def retranslateUi(self, MainWindow):        # 定义retranslateUi的方法，用于设置UI界面的文本内容
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "py一键转exe"))
        self.pushButton.setText(_translate("MainWindow", "打开文件"))
        self.pushButton_2.setText(_translate("MainWindow", "设置ICO图标"))
        self.pushButton_3.setText(_translate("MainWindow", "一键生成"))
    """
    下面的函数与上面的按钮点击事件连接起来
    """
    def set_icon_path(self):                  # 定义set_icon_path的方法，将选择ICO图标文件并在lineEdit_2控件中显示对应的路径
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        icon_path, _ = QFileDialog.getOpenFileName(None, "选择ICO图标文件", "", "Icon Files (*.ico);;All Files (*)",
                                                   options=options)
        if icon_path:
            self.lineEdit_2.setText(icon_path)

    def open_filr(self):
        options = QFileDialog.Options()       # 与上面函数相同，定义open_filr方法，选择Python文件并在lineEdit控件中显示对应的路径
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "选择文件", "", "Python Files (*.py);;All Files (*)", options=options)
        if file_name:
            self.lineEdit.setText(file_name)

    def convert_to_exe(self):       # 定义convert_to_exe的方法，用于将Python文件转换为exe文件
        file_path = self.lineEdit.text()
        icon_path = self.lineEdit_2.text()
        #下述代码判断两个函数是否出现未填或空白，如果为空弹出警告窗口并返回
        if not file_path:
            QMessageBox.warning(None, "警告", "请设置要转换的文件！")
            return
        if not icon_path:
            QMessageBox.warning(None, "警告", "请设置ICO图标文件！")
            return
        try:
            PyInstaller.__main__.run([file_path, '--onefile', '--icon=' + icon_path, '--noconsole'])
            #--onefile 表示将所有依赖项打包成一个单独的可执行文件    --icon 用于指定可执行文件的图标    --noconsole 表示在运行可执行文件时不显示控制台窗口   (注：可按照自己的需求改)
            """下述代码中 如果打包成功，它会在textBrowser控件中显示一段话，并弹出一个窗口显示成功信息  如果发生异常，它会捕获异常并在弹出窗口中显示失败信息"""
            self.textBrowser.setText("文件已放.\dist目录下&#128579;")
            QMessageBox.information(None, "成功", "转换成功！")
        except Exception as e:
            QMessageBox.critical(None, "错误", f"转换失败：{e}")

if __name__ == "__main__":          # 如果当前脚本为主程序，则执行以下代码
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()        # 创建一个Ui_MainWindow对象
    ui.setupUi(MainWindow)          # 调用setupUi方法设置UI界面
    MainWindow.show()       # 显示主窗口
    sys.exit(app.exec_())   # 进入事件循环，等待用户操作
