import matplotlib
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from gui import Ui_Dialog
from drawing.drawer import Drawer as drawer

matplotlib.use('TkAgg')


class GuiProgram(Ui_Dialog):
    """ Класс контроллер - интерпретирует действия пользователя """

    def __init__(self, dialog: QtWidgets.QDialog) -> None:
        """ Вызывается при создании нового объекта класса """
        # Создание окна
        Ui_Dialog.__init__(self)
        # Установка пользовательского интерфейс


        self.setupUi(dialog)

        # ПОЛЯ КЛАССА
        # Параметры 1 графика
        self.drawer_1 = drawer(
            layout=self.layout_plot_1,
            widget=self.widget_plot_1
        )
        # ПАРАМЕТРЫ ГРАФИКА 2
        self.drawer_2 = drawer(
            widget=self.widget_plot_2,
            layout=self.layout_plot_2
        )

        self.gamma_difference = []
        self.gamma_with_gas = []
        self.gamma_without_gas = []
        self.frequency = []
        self.value_threshold = None

        self.btn_with_gas.clicked.connect(self.push_with_gas)
        self.btn_without_gas.clicked.connect(self.push_without_gas)
        self.btn_difference.clicked.connect(self.difference)
        self.pushButton_threshold.clicked.connect(self.threshold)

    def push_with_gas(self):
        # path_file, _ = QFileDialog.getOpenFileName()
        path_file = "C:/DEV/pro_line_graph-master/25empty.csv"
        self.frequency, self.gamma_with_gas = self.data_from_file(path_file)

        self.gas()

    def push_without_gas(self):
        # path_file, _ = QFileDialog.getOpenFileName()
        path_file = "C:/DEV/pro_line_graph-master/25DMSO.csv"
        self.frequency, self.gamma_without_gas = self.data_from_file(path_file)

        self.gas()

        # ПАРСИНГ ДАННЫХ

    def data_from_file(self, path_file: str):
        file = open(path_file, "r")
        file.readline()

        line = file.readline()
        frequency_array = []
        gamma_array = []
        while line[0] != "*":
            val = line.split()
            frequency_array.append(float(val[1]))
            gamma_array.append(float(val[4]))
            line = file.readline()

        file.close()

        return frequency_array, gamma_array

        # РИСУЕМ ГРАФИКИ

    def gas(self):
        if self.gamma_with_gas is None and self.gamma_without_gas is None:

            return
        if self.gamma_with_gas and self.gamma_without_gas:

            # рисуем 2
            self.drawer_1.draw_2_line_xyy(
                self.frequency, self.gamma_with_gas, self.gamma_without_gas
            )
        elif self.gamma_with_gas:

            # рисуем 1 график c веществом
            self.drawer_1.draw_line_xy(self.frequency, self.gamma_with_gas)
        elif self.gamma_without_gas:
            # рисуем 1 график пустой

            self.drawer_1.draw_line_xy(self.frequency, self.gamma_without_gas)

    def difference(self):
        gamma_with_gas = np.array(self.gamma_with_gas)
        gamma_without_gas= np.array(self.gamma_without_gas)

        self.gamma_difference = abs(gamma_with_gas - gamma_without_gas)

        self.drawer_2.draw_line_xy(self.frequency, self.gamma_difference)

    def threshold(self):
        percent_threshold = float(self.lineEdit_threshold.text())
        self.value_threshold = np.max(self.gamma_difference) * (percent_threshold/100)
        self.drawer_2.draw_xy_and_line(self.frequency, self.gamma_difference, self.value_threshold)
