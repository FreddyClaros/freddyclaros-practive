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

from src.classes.transport import Transport


class Land(Transport):
    def __init__(self, name, price, hasMotor):
        super().__init__(name, price)
        self._motor: bool = hasMotor

    def getHasMotor(self):
        return self._motor

    def displayData(self):
        return "name: " + self.getName() + " /prince: " + str(self.price) + " /has motor?: " + str(
            self._motor)
