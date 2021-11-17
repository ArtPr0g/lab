def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for dictionary in items:
            note = dictionary.get(args[0])
            if note is not None:
                yield note
    else:
        for d in items:
            dictionary = dict()
            for arg in args:
                note = d.get(arg)
                if note is not None:
                    dictionary[arg] = note
            if len(dictionary) != 0:
                yield dictionary


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 5000, 'color': 'red'},
        {'title': 'Диван для отдыха', 'price': 10000, 'color': 'white'},
        {'title': None, 'price': None, 'color': 'black'},
        {'title': 'Кровать', 'price': 15000, 'color': 'yellow'}
    ]
    data1 = list()
    data2 = list()

    for i in field(goods, 'title'):
        data1.append(i)
    print(str(data1))


    for i in field(goods, 'title', 'price','color'):
        data2.append(i)
    print(data2)