## используется для сортировки
from operator import itemgetter

class Composition:
    """Музыкальное произведение"""

    def __init__(self, id, naz, count):
        self.id = id
        self.naz = naz
        self.count = count


class Orchestra:
    """Оркестр"""
    def __init__(self, id,name):
        self.id = id
        self.name = name # название

class OrchestraComposition:
    """
 'Исполнители произведения' для реализации
 связи многие-ко-многим
    """

    def __init__(self, orc_id, comp_id):
        self.orc_id = orc_id
        self.comp_id = comp_id


# Оркестр
orc = [
    Orchestra(1, 'народный'),
    Orchestra(2, 'камерный'),
    Orchestra(3, 'военный'),
    Orchestra(4, 'эстрадный'),
    Orchestra(5, 'симфонический'),
]

# Музыкальные композиции
comp = [
    Composition(1, 'Лунная соната', 3),
    Composition(2, 'Танец рыцарей', 4),
    Composition(3, 'Марш Мендельсона', 2),
    Composition(4, 'Пятая симфония', 5),
    Composition(5, 'Щелкунчик', 4),
    Composition(6, 'Новый мерин', 3),
    Composition(7, 'Ария', 2),
    Composition(8, 'Кан-кан', 1)
]

оrchestro_сomposition = [
    OrchestraComposition(1, 1),
    OrchestraComposition(2, 2),
    OrchestraComposition(3, 4),
    OrchestraComposition(4, 1),
    OrchestraComposition(5, 3),
    OrchestraComposition(6, 1),
    OrchestraComposition(7, 2),
    OrchestraComposition(8, 3),
    OrchestraComposition(7, 5),
    OrchestraComposition(6, 2),
]
def Task1(one_to_many):
    print('Задание В1')
    res_11 = []
    for naz, count, orc_name in one_to_many:
        if 'А' in naz[0]:
            res_11.append((naz, orc_name))
    return res_11
def Task2(one_to_many):
    print('Задание В2')
    buff = []
    for o in orc:
        # список видов транспорта
        o_names = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_names) > 0:
            o_count = [count for _, count, _ in o_names]
            min_count = min(o_count)
            buff.append((o.name, min_count))
    res_12 = sorted(buff, key=itemgetter(1))
    return res_12
def Task3(many_to_many):
    print('Задание В3')
    buff = []
    for naz, count, orc_name in many_to_many:
        buff.append((naz, orc_name))
    res_13 = list(sorted(buff, key=itemgetter(0)))
    return res_13

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.naz, c.count, o.name)
                   for o in orc
                   for c in comp
                   if c.count == o.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, oc.orc_id, oc.comp_id)
                         for o in orc
                         for oc in оrchestro_сomposition
                         if o.id == oc.orc_id]

    many_to_many = [(c.naz, c.count, orc_name)
                    for orc_name, orc_id, comp_id in many_to_many_temp
                    for c in comp if c.id == comp_id]


    print('Test')#вывод списков со связями 1-м, м-м
    res_0 = (one_to_many)
    print(res_0)
    res_01 = (many_to_many)
    print(res_01)

    Task1(one_to_many)

    Task2(one_to_many)

    Task3(many_to_many)

if __name__ == '__main__':
    main()
