import doctest


class Desk:
    def __init__(self, desk_hight: float, box_opened: bool):
        """
        Создание и подготовка к работе объекта "Стол"

        :param capacity_volume: Текущая высота стола
        :param occupied_volume: Состояние ящика (открыт: True, закрыт: False)

        Примеры:
        >>> desk = Desk(750, False)  # инициализация экземпляра класса
        """
        if not isinstance(desk_hight, (int, float)):
            raise TypeError("Высота стола должна быть типа int или float")
        if not (100 <= desk_hight <= 1000):
            raise ValueError("Высота стола должна быть положительным числом не более 1000 и не менее 100")
        self.desk_hight = desk_hight

    def is_box_opened(self) -> bool:
        """
        Функция которая проверяет, открыт ли ящик

        :return: Открыт ли ящик

        Примеры:
        >>> desk = Desk(500, False)
        >>> desk.is_box_opened()
        """
        ...

    def change_desk_hight(self, new_hight: float) -> None:
        """
        Изменение высоты стола.
        :param new_hight: Заданная высота стола

        :raise ValueError: Если заданная высота более 1000 или менее 100, вызываем ошибку

        Примеры:
        >>> desk = Desk(500, False)
        >>> desk.change_desk_hight(200)
        """
        if not isinstance(new_hight, (int, float)):
            raise TypeError("Высота стола должна быть типа int или float")
        if not (100 <= new_hight <= 1000):
            raise ValueError("Высота стола должна быть положительным числом не более 1000 и не менее 100")
        ...

    def change_box_status(self, estimate_box_status: bool) -> None:
        # вот здесь комментарии перепиши, у меня заплетак языкается
        """
        Изменение положения ящика.

        :param estimate_box_status: Новое состояние ящика (открыт/закрыт)
        :raise ValueError: Если ящик уже находится в требуемом положении, то вызываем ошибку.

        :return: Новое положение ящика

        Примеры:
        >>> desk = Desk(500, True)
        >>> desk.change_box_status(False)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
