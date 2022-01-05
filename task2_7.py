from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def outgo(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def outgo(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def outgo(self):
        return 2 * self.h + 0.3

    def sum_outgo(self, total_cloth):
        i = 0
        for el in total_cloth:
            i += el.outgo
        return i


coat = Coat(55)
suit_1 = Costume(1.84)
suit_2 = Costume(1.57)
suit_3 = Costume(2.72)
suit_4 = Costume(2.11)
total_cloth = [suit_1, suit_2, suit_3, suit_4]
print(coat.outgo)
print(suit_1.outgo)
print(suit_1.sum_outgo(total_cloth))

