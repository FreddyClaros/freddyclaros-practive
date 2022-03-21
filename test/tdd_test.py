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
    def test_add(self):
        add = TddPractice()
        result = add.add(2, 2)
        self.assertEqual(4, result)

    def test_add(self):
        add = TddPractice()
        result = add.add(5, 2)
        self.assertEqual(7, result)


if __name__ == '__main__':
    unittest.main()
