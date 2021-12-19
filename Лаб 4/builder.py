from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def processor(self) -> None:  # процессор
        pass

    @abstractmethod
    def videocard(self) -> None:  # видеокарта
        pass

    @abstractmethod
    def computer(self) -> None:  # компьютер
        pass


class Computer_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Shop()

    @property  # property позволяет превратить метод класса в атрибут класса
    def product(self) -> Shop:
        product = self._product
        self.reset()
        return product

    def processor(self) -> None:
        self._product.add("процессор")

    def videocard(self) -> None:
        self._product.add("видеокарта")

    def computer(self) -> None:
        self._product.add("компьютер")


class Shop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property  # property позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def Electro(self) -> None:
        self.builder.videocard()
        self.builder.processor()

    def Elcomp(self) -> None:
        self.builder.computer()
        self.builder.videocard()


if __name__ == "__main__":
    director = Director()
    builder = Computer_Builder()
    director.builder = builder

    print("Электро: ")
    director.Electro()
    builder.product.list_parts()

    print("\n\nЭлкомп: ")
    director.Elcomp()
    builder.product.list_parts()


