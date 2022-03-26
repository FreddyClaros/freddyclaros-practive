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
from src.classes.land import Land
from src.classes.bicycle import Bicycle
from src.classes.car import Car
from src.classes.list_land_transport import ListLandTransport

if __name__ == "__main__":
    transport1: Land = Land("Trailer", 200, True)
    transport2: Bicycle = Bicycle("Bike", 50, False, True)
    transport3: Car = Car("Petita", 100, True, True)

    transportList = [transport1, transport2, transport3]

    transport4: Car = Car("Tesla", 200, True, True)

    listOfTransports: ListLandTransport = ListLandTransport(transportList)
    listOfTransports.addLand(transport4)
    listOfTransports.display()