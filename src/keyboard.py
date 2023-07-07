from src.item import Item


class MixinLanguage:
    """
    Класс с дополнительным функционалом для класса Keyboard.
    """

    def __init__(self):
        """
        Инициализирует класс.

        Содержит свойства:
        self.__language - язык раскладки клавиатуры, по умолчанию "EN".
        """

        self.__language = "EN"

    @property
    def language(self):
        """
        Возвращает язык раскладки клавиатуры.
        """
        
        return self.__language

    @language.setter
    def language(self, language):
        """
        Сообщает о невозможности изменить язык раскладки клавиатуры за пределами класса.
        """

        raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        """
        Изменяет язык раскладки клавиатуры.
        """

        if self.__language == "EN":
            self.__language = "RU"
            return self
        else:
            self.__language = "EN"
            return self


class Keyboard(Item, MixinLanguage):
    """
    Класс для представления товара “клавиатура”.

    Наследует свойства класса Item.
    Наследует свойства экземпляра класса Item.
    Наследует свойства и методы экземпляра класса MixinLanguage.
    """

    def __init__(self, name, price, quantity):
        """
        Инициализирует экземпляр класса Keyboard.
        """

        super().__init__(name, price, quantity)
