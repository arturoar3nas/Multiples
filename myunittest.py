#!/usr/bin/python3

import logging
import argparse
import unittest

from multiples import multiple

print(__name__)
print('Write a program that prints all the numbers from 1 to 100. However, for\
 multiples of 3, instead of the number, print "Linio". For multiples of 5 print\
 "IT". For numbers which are multiples of both 3 and 5, print "Linianos"')

# create logger with 'spam_application'
logger = logging.getLogger('linio.py')
logger.setLevel(logging.DEBUG)


class MultiplesTest(unittest.TestCase):
    # multiplos de 3
    def test_1(self):
        # Imprime todo y tiene 47 elementos (incluye el cero)
        self.assertEqual(47, multiple(100, [3, 5]))
    def test_2(self):
        # Imprime solo multiplos de 5 y retorna 20 elemntos
        self.assertEqual(20, multiple(100, [0, 5]))

    def test_sum_to_10(self):
        # Imprime solo multiplos de 3 y retorna 33 elementos
        self.assertEqual(33, multiple(100, [3, 0]))

    def test_sum_to_100(self):
        # No imprime multiplos y retorna 0 elemtnos
        self.assertEqual(0, multiple(100, [0, 0]))


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    config = {}
    unittest.main()
