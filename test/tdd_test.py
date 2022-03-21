#
# @tdd_practice.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import unittest
from src.tdd import TddPractice
from src.tdd import ArrayNumbers


class TddTest(unittest.TestCase):
    def test_add(self): #exercise 1
        add = TddPractice()
        result = add.add(2, 2)
        self.assertEqual(4, result)

    def test_add(self):
        add = TddPractice()
        result = add.add(5, 2)
        self.assertEqual(7, result)

    def test_validate_age(self): #exercise 2
        validate = TddPractice()
        result = validate.validate_age(5)
        self.assertTrue(result)

    def test_validate_age(self):
        validate = TddPractice()
        result = validate.validate_age(-5)
        self.assertFalse(result)

    def test_validate_age(self):
        validate = TddPractice()
        result = validate.validate_age(0)
        self.assertFalse(result)

    def test_validate_age(self):
        validate = TddPractice()
        result = validate.validate_age(100)
        self.assertTrue(result)

    def test_validate_age(self):
        validate = TddPractice()
        result = validate.validate_age(101)
        self.assertFalse(result)

    def test_max(self): #exercise 3
        maximum = TddPractice()
        result = maximum.max(101, 10, 500)
        self.assertEqual(500, result)

    def test_max(self):
        maximum = TddPractice()
        result = maximum.max(-20, 1, -500)
        self.assertEqual(1, result)

    def test_max(self):
        maximum = TddPractice()
        result = maximum.max(-20, -91, -500)
        self.assertEqual(-20, result)

    def test_max(self):
        maximum = TddPractice()
        result = maximum.max(50, 52, -500)
        self.assertEqual(52, result)

    def test_isVocal(self): #exercise 4
        vocal = TddPractice()
        result = vocal.isVocal('a')
        self.assertTrue(result)

    def test_isVocal(self):
        vocal = TddPractice()
        result = vocal.isVocal('b')
        self.assertFalse(result)

    def test_isVocal(self):
        vocal = TddPractice()
        result = vocal.isVocal('T')
        self.assertFalse(result)

    def test_isVocal(self):
        vocal = TddPractice()
        result = vocal.isVocal('A')
        self.assertTrue(result)

    def test_isVocal(self):
        vocal = TddPractice()
        result = vocal.isVocal(12)
        self.assertFalse(result)

    def test_isVocal(self):
        vocal = TddPractice()
        result = vocal.isVocal('@')
        self.assertFalse(result)

    def test_inversa(self): #exercise 5
        inverse = TddPractice()
        result = inverse.inversa('abcd')
        self.assertEqual('dcba', result)

    def test_inversa(self):
        inverse = TddPractice()
        result = inverse.inversa('()@##')
        self.assertEqual('##@)(', result)

    def test_inversa(self):
        inverse = TddPractice()
        result = inverse.inversa('aFcd10')
        self.assertEqual('01dcFa', result)

    def test_inversa(self):
        inverse = TddPractice()
        result = inverse.inversa('a  10')
        self.assertEqual('01  a', result)

    def test_inversa(self):
        inverse = TddPractice()
        result = inverse.inversa('a  fd10')
        self.assertNotEqual('a fd 10', result)

    def test_inversa(self):
        inverse = TddPractice()
        result = inverse.inversa('AT16 Python')
        self.assertEqual('nohtyP 61TA', result)

    def test_palindrome(self): #exercise 6
        pal = TddPractice()
        result = pal.palindrome('madam')
        self.assertEqual('madam', result)

    def test_palindrome(self):
        pal = TddPractice()
        result = pal.palindrome('oruro')
        self.assertEqual('oruro', result)

    def test_palindrome(self):
        pal = TddPractice()
        result = pal.palindrome('Oruro') #not counting the capital latters
        self.assertNotEqual('orurO', result)

    def test_palindrome(self):
        pal = TddPractice()
        result = pal.palindrome('Mom')
        self.assertNotEqual('moM', result)

    def test_array_numbers(self): #exercise 7
        array = [3, 4, 6, 5, 7]
        result = ArrayNumbers(array)
        self.assertEqual(7, result.getmax())
        self.assertEqual(3, result.getmin())
        self.assertEqual(5, result.getaverage())

    def test_array_numbers(self):
        array = [-6, 4, -8, 10, 2, -5]
        result = ArrayNumbers(array)
        self.assertEqual(10, result.getmax())
        self.assertEqual(-8, result.getmin())
        self.assertEqual(-0.5, result.getaverage())

    def test_array_numbers(self):
        array = [-6, -3, -5, -6, -7]
        result = ArrayNumbers(array)
        self.assertEqual(-3, result.getmax())
        self.assertEqual(-7, result.getmin())
        self.assertEqual(-5.4, result.getaverage())


if __name__ == '__main__':
    unittest.main()
