"""
Создать класс ​ TrafficLight ​ (светофор) и определить у него один атрибут ​ color ​ (цвет) и метод
running ​ (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) ​ — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

from _tkinter import TclError
from itertools import cycle
from time import sleep
from tkinter import Tk, Frame, BOTH, Canvas


class Window(Frame):
    color_upper = 'grey70'
    color_middle = 'grey70'
    color_lower = 'grey70'
    canvas = None

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title(f'Traffic light')
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.canvas.create_rectangle(30, 30, 210, 570, fill='grey')
        self.canvas.pack(fill=BOTH, expand=1)

    def update(self):
        self.canvas.create_oval(40, 40, 200, 200, fill=self.color_upper)
        self.canvas.create_oval(40, 210, 200, 380, fill=self.color_middle)
        self.canvas.create_oval(40, 390, 200, 550, fill=self.color_lower)
        self.canvas.update()

    def set_color_upper(self, color):
        self.color_upper = color

    def set_color_middle(self, color):
        self.color_middle = color

    def set_color_lower(self, color):
        self.color_lower = color


class TrafficLight:
    off = 'grey70'
    intervals = [7, 2, 7, 2]
    colors = [['red', off, off], [off, 'yellow', off], [off, off, 'green'], [off, 'yellow', off]]

    def running(self, inst):
        for k, i in cycle(enumerate(self.colors)):
            upper, middle, lower = self.colors[k]
            inst.set_color_upper(upper)
            inst.set_color_middle(middle)
            inst.set_color_lower(lower)
            inst.update()
            sleep(self.intervals[k])


def main():
    root = Tk()
    window = Window(root)
    root.geometry("250x610+300+300")
    window.update()
    traffic_light = TrafficLight()
    traffic_light.running(window)
    root.mainloop()

try:
    main()
except TclError:
    print('Good bye!')
