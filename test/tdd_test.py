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


if __name__ == '__main__':
    unittest.main()
