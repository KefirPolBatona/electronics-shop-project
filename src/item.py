import csv

import src


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """

        result = int(self.price * self.quantity)
        return result

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)
        return self.price

    @property
    def name(self):
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Принимает новое название товара.
        Сохраняет название товара с количеством символов не более 10
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляр класса Item с данными из файла _src/items.csv_
        """

        with open('../src/items.csv', newline='', encoding='windows-1251') as csv_file:
            reader_csv_file = csv.DictReader(csv_file)
            for row in reader_csv_file:
                name, price, quantity = row.split(',')
                cls(name, price, quantity)




                # return print()





    # `string_to_number()` - статический метод, возвращающий число из числа-строки