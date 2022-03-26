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

class Car(Land):
    def __init__(self, name, price, hasMotor, useGas):
        super().__init__(name, price, hasMotor)
        self._useGas: bool = useGas

    def displayData(self):
        return "name: " + self.getName() + " /price: " + str(self.price) + " /has motor?: " + str(
            self.getHasMotor()) + " /use gas?: " + str(self._useGas)
