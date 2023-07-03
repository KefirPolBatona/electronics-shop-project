from src.phone import Phone


class TestPhone:
    """
    Класс для тестирования методов класса Phone.
    """

    def test_init(self):
        """
        Проверяет значения аргументов экземпляра класса.
        """
        phone1 = Phone("iPhone 14", 150_000, 15, 2)
        assert str(phone1) == "iPhone 14"
        assert phone1.price == 150000
        assert phone1.quantity == 15
        assert phone1.number_of_sim == 2

    def test_repr(self):
        """
        Проверяет значение метода repr.
        """
        phone1 = Phone("iPhone 14", 125_000, 45, 1)
        assert repr(phone1) == "Phone('iPhone 14', 125000, 45, 1)"

