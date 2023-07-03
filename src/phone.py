from src.item import Item


class Phone(Item):
    """
    Класс для представления товара в магазине.
    Принимает:
        number_of_sim - количество поддерживаемых сим-карт.
    Наследует свойства класса:
        pay_rate - скидка,
        all - список экземпляров.
    Наследует свойства экземпляра класса:
        self.__name - Название товара,
        self.price - Цена за единицу товара,
        self.quantity: Количество товара в магазине.
    """

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Создание экземпляра класса item.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает атрибуты экземпляра класса
        """
        return super().__repr__().replace(")", f", {self.__number_of_sim})")

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
