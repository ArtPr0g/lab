from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()#пустое множество
        self.data = items
        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        it = iter(self.data)
        while True:
            try:
                current = next(it)
            except StopIteration:
                raise StopIteration
            else:
                if self.ignore_case is True and isinstance(current, str):
                    current = current.lower()
                if current not in self.used_elements:
                    self.used_elements.add(current)
                    return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(5, 1, 10)
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print(list(Unique(data1)))
    print(list(Unique(data2)))
    print(list(Unique(data3, ignore_case=True)))
    print(list(Unique(data3, ignore_case=False)))