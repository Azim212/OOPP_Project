import shelve
simStorage = shelve.open('SimStorage')


# Data for light bulbs and their wattage: 'https://www.noao.edu/education/QLTkit/ACTIVITY_Documents/Energy/TypesofLights.pdf'
class lightbulb:
    def __init__(self, type, watt, amount):
        self.__type = type
        self.__watt = watt
        self.__amount = amount

    def get_watt(self):
        return self.__watt

    def get_amount(self):
        return self.__amount


class led(lightbulb):
    def __init__(self, amount):
        super().__init__('LED', 6, amount)


class cfl(lightbulb):
    def __init__(self, amount):
        super().__init__('CFL', 9, amount)


class incandescent(lightbulb):
    def __init__(self, amount):
        super().__init__('Incandescent', 40, amount)


def calcPrice():
    ledEx = led(simStorage['ledNum'])
    cflEx = cfl(simStorage['cflNum'])
    incEx = incandescent(simStorage['incNum'])

    hrs = 8  # Assuming 8 hours used for light bulb a day
    cost = 0.30  # $ per kWh. Data received from 'http://energyusecalculator.com/global_electricity_prices.htm'

    calcLED = (ledEx.get_watt() / 1000) * cost * hrs  #
    calcCFL = (cflEx.get_watt() / 1000) * cost * hrs  # Cost per day
    calcINC = (incEx.get_watt() / 1000) * cost * hrs  #

    amtLED = ledEx.get_amount()
    amtCFL = cflEx.get_amount()
    amtINC = incEx.get_amount()

    finalPrice = calcLED * amtLED + calcCFL * amtCFL + calcINC * amtINC
    return round(finalPrice, 2)














































