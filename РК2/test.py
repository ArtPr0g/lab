import unittest
import sys, os

sys.path.append(os.getcwd())
from main import *


class Test_task_1(unittest.TestCase):
    def test_task_1(self):
        one_to_many = [(c.naz, c.count, o.name)
                       for o in orc
                       for c in comp
                       if c.count == o.id]
        self.assertEqual(Task1(one_to_many), [('Ария', 'камерный')])

class Test_task_2(unittest.TestCase):
    def test_task_2(self):
        one_to_many = [(c.naz, c.count, o.name)
                       for o in orc
                       for c in comp
                       if c.count == o.id]
        self.assertEqual(Task2(one_to_many),[('народный', 1), ('камерный', 2), ('военный', 3), ('эстрадный', 4), ('симфонический', 5)])


class Test_task_3(unittest.TestCase):
    def test_task_3(self):
        many_to_many_temp = [(o.name, oc.orc_id, oc.comp_id)
                             for o in orc
                             for oc in оrchestro_сomposition
                             if o.id == oc.orc_id]
        many_to_many = [(c.naz, c.count, orc_name)
                        for orc_name, orc_id, comp_id in many_to_many_temp
                        for c in comp if c.id == comp_id]
        self.assertEqual(Task3(many_to_many),
                         [('Лунная соната', 'народный'), ('Лунная соната', 'эстрадный'), ('Марш Мендельсона', 'симфонический'), ('Пятая симфония', 'военный'), ('Танец рыцарей', 'камерный')])
if __name__ == "__main__":
    unittest.main()