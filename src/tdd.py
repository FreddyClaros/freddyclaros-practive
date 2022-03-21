#
# @tdd.py Copyright (c) 2022 Jalasoft.
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

class TddPractice:
    def add(self, number1, number2):
        return number1 + number2

    def validate_age(self, age): #validate age between 0 and 100 inclusive
        return 0 < age <= 100

    def max(self, number1, number2, number3):
        list = [number1, number2, number3]
        return max(list)

    def isVocal(self, char):
        list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        return char in list

    def inversa(self, str):
        return str[::-1]

    def palindrome(self, str):
        return str == str[::-1]

    def array_numbers(self, list):
        return ArrayNumbers(list)

class ArrayNumbers:

    def __init__(self, array):
        self.array = array

    def getmax(self):
        return max(self.array)

    def getmin(self):
        return min(self.array)

    def getaverage(self):
        return sum(self.array) / len(self.array)
