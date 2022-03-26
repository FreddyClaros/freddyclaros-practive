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

from src.classes.land import Land

class ListLandTransport():
    def __init__(self, list):
        self._list = list

    def addLand(self, newLand):
        self._list.append(newLand)

    def display(self):
        for land in self._list:
            print(land.displayData())
