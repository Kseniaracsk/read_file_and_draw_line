import matplotlib
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

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        self.btn_download.clicked.connect(self.draw)

    def draw(self):
        """ Рисуем график """
        # Вызов окна выбора файла
        file_name, filetype = QFileDialog.getOpenFileName(None,
                                                          "Выбрать файл",
                                                          ".",
                                                          "All Files(*)")

        # ЧИТАЮ ФАЙЛ
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        # ВЫВОДИМ
        array1 = [0]*len(lines)
        array2 = [0] * len(lines)
        for i in range(len(lines)):
            val = lines[i].split()
            array1[i]=float(val[0])
            array2[i]=float(val[1])

        self.drawer_1.draw_line2(array1,array2)

