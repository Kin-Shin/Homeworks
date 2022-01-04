class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print('Используется инструмент "ручка"')


class Pencil(Stationery):
    def draw(self):
        print('Используется инструмент "карандаш"')


class Handle(Stationery):
    def draw(self):
        print('Используется инструмент "маркер"')


render = Stationery("Rendering")
print(render.title)
render.draw()
pen = Pen("Pen").draw()
pencil = Pencil("Pencil").draw()
handle = Handle("Handle").draw()
