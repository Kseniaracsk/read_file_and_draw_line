# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 437)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_plot_1 = QtWidgets.QWidget(Dialog)
        self.widget_plot_1.setObjectName("widget_plot_1")
        self.layout_plot_1 = QtWidgets.QVBoxLayout(self.widget_plot_1)
        self.layout_plot_1.setObjectName("layout_plot_1")
        self.verticalLayout.addWidget(self.widget_plot_1)
        self.btn_download = QtWidgets.QPushButton(Dialog)
        self.btn_download.setObjectName("btn_download")
        self.verticalLayout.addWidget(self.btn_download)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_download.setText(_translate("Dialog", "Загрузка из файла"))
