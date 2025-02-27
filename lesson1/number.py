"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, argument):
        self.value = self.value + argument
        return self.value

    def substract(self, argument):
        self.value = self.value - argument
        return self.value


n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5

#Здесь вопрос: зачем писать методы add, substract, если есть магические __add__, __sub__?