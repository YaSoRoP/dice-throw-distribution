from typing import Union
from random import shuffle, choice


class Cube:
    """Класс представления игральной кости"""
    
    performance: dict = {
        "One": 0,
        "Two": 0,
        "Three": 0,
        "Four": 0,
        "Five": 0,
        "Six": 0
    }
    
    
    def __check_value(cls, value: Union[int, float]) -> bool:
        """Проверяет входяще значение для rool_dice

        Args:
            value (Union[int, float]): вводимые данные: int, float

        Returns:
            bool: True: value is int > 0 False not is int < 1
        """
        return type(value) is int and value > 0
    
    
    def roll_dice(self, quantity: int) -> dict:
        """Имитация подкидывания игральной кости

        Args:
            quantity (int): кол-во подбрасываний игральной кости

        Raises:
            TypeError: quantity not is int
        """
        if self.__check_value(quantity):
            keys_performance: list = list(self.performance.keys())
            for _ in range(quantity):
                shuffle(keys_performance)
                self.performance[choice(keys_performance)] += 1
        else:
            raise TypeError('Неверный формат вводимых данных!')
        
        return self.performance