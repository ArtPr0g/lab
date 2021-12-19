class Computer():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """
    def operation(self) -> str:
        pass


class Computer(Computer):
    """
       Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
       быть несколько вариаций этих классов.
       """
    def operation(self) -> str:
        return "Computer"


class Decorator(Computer):
    """Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """
    _component: Computer = None

    def __init__(self, component: Computer) -> None:
        self._component = component

    @property    #превращает метод класса в атрибут класса.
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Processor(Decorator):
    def operation(self) -> str:
        return f"Processor({self.component.operation()})"


class Videocard(Decorator):
    def operation(self) -> str:
        return f"Videocard({self.component.operation()})"


def show(component: Computer) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    simple = Computer()
    print("Client: I've got a simple component:")
    show(simple)
    print("\n")
    # ...так и декорированные.
    #
    # Декораторы могут обёртывать не только простые
    # компоненты, но и другие декораторы.
    decorator1 = Processor(simple)
    decorator2 = Videocard(decorator1)
    print("Client: Now I've got a decorated component:")
    show(decorator2)