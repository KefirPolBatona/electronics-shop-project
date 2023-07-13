import csv
import os


class InstantiateCSVError(Exception):
    """
    Класс исключения при получении поврежденного файла `item.csv`.
    """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл поврежден'

    def __str__(self):
        return self.message


class Item:
    """
    Родительский класс для представления товара в магазине.

    Свойства:
    pay_rate - размер скидки на товар,
    all - список экземпляров класса.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализирует экземпляр класса item.
        Наследует класс MixinLanguage в src.keyboard - "super().__init__()".

        Создает свойства:
        self.__name - Название товара,
        self.price - Цена за единицу товара,
        self.quantity - Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """
        Возвращает атрибуты экземпляра класса
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает название товара
        """
        return self.__name

    def __add__(self, other):
        """
        Определяет общее количество двух товаров.
        """
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает и возвращает общую стоимость конкретного товара в магазине.
        """

        result = int(self.price * self.quantity)
        return result

    def apply_discount(self) -> float:
        """
        Применяет скидку, установленную для конкретного товара.
        Возвращает стоимость со скидкой.
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
    def instantiate_from_csv(cls, file_csv='items.csv'):
        """
        Инициализирует экземпляр класса Item с данными из файла _src/items.csv_
        """

        cls.all.clear()

        try:
            open(os.path.join('..', 'src', file_csv), newline='', encoding="utf-8")
        except:
            raise FileNotFoundError(f"Отсутствует файл {file_csv}")
        else:
            with open(os.path.join('..', 'src', file_csv), newline='', encoding="utf-8") as csv_file:
                reader_csv_file = csv.DictReader(csv_file)
                for row in reader_csv_file:
                    if len(row) == 3 and row['name'] and row['price'] and row['quantity']:
                        name = row['name']
                        price = cls.string_to_number(row['price'])
                        quantity = cls.string_to_number(row['quantity'])
                        cls(name, price, quantity)
                    else:
                        raise InstantiateCSVError(f"Файл {file_csv} поврежден")

    @staticmethod
    def string_to_number(string):
        """
        Возвращающий число из числа-строки
        """

        return int(float(string))
