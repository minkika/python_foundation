"""
Реализовать класс ​ Stationery ​ (канцелярская принадлежность). Определить в нем атрибут ​
title (название) и метод ​ draw ​ (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса ​ Pen ​ (ручка), ​ Pencil ​ (карандаш), ​ Handle ​ (маркер). В каждом из классов
реализовать переопределение метода ​ draw​ . Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""

from tkinter import Tk, Button
import path


class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self, color, width, instance):
        path.move(color, width, instance)


class Pen(Stationery):

    def draw(self):
        super().draw('blue', 3, self.title)


class Pencil(Stationery):

    def draw(self):
        super().draw('grey', 5, self.title)


class Handle(Stationery):

    def draw(self):
        super().draw('pink', 8, self.title)


pen = Pen('Stabilo pen')
pencil = Pencil('Koh-i-noor pencil')
handle = Handle('Attache handle')

root = Tk()

b1 = Button(text="Pencil", width=15, height=3)
b2 = Button(text="Pen", width=15, height=3)
b3 = Button(text="Handle", width=15, height=3)

b1.config(command=pencil.draw)
b2.config(command=pen.draw)
b3.config(command=handle.draw)

b1.pack()
b2.pack()
b3.pack()

root.mainloop()
