import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

with open('data_light.json', encoding='utf-8') as file:
    data = json.load(file)

@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=str.lower)

@print_result
def f2(arg):
    return list(filter(lambda string: str.startswith(str.lower(string), 'программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda string: string + " с опытом Python", arg))

@print_result
def f4(arg):
    #объединение элементов из нескольких источников данных.
    return dict(zip(arg, list('зарплата {} руб.'.format(val) for val in gen_random(len(arg), 1000000, 2000000))))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))