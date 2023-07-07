from src.keyboard import Keyboard

# Данные для тестов
kb = Keyboard('Абра-Катабра', 9600, 5)


class TestKeyboard:
    """
    Класс для тестирования класса Keyboard.
    """

    def test_init(self):
        """
        Проверяет значения аргументов экземпляра класса.
        """

        assert f'{str(kb)} за {kb.price}' == "Абра-Катабра за 9600"
        assert kb.quantity == 5

    def test_language(self):
        """
        Проверяет язык раскладки.
        """

        assert str(kb.language) == "EN"

    def test_change_lang(self):
        """
        Проверяет изменение языка раскладки.
        """

        kb.change_lang()
        assert str(kb.language) == "RU"

        kb.change_lang().change_lang()
        assert str(kb.language) == "RU"

