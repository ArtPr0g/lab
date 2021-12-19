import unittest
import sys, os
from builder import *

sys.path.append(os.getcwd())

class Computer_Builder_Test(unittest.TestCase):
    director = Director()
    builder = Computer_Builder()
    director.builder = builder
    def test_Lasurit(self):
       print("Электро: ")
       self.director.Electro()
       self.builder.product.list_parts()

    def test_Shatura(self):
        print("\nЭлкомп: ")
        self.director.Elcomp()
        self.builder.product.list_parts()

if __name__ == "__main__":
    unittest.main()