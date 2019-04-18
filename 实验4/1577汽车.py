#!/anaconda3/bin/python
# @Time    : 2019-04-04 12:54
# @Author  : zhou
# @File    : 1577汽车
# @Software: PyCharm
# @Description: 


class Veicle:
    """载具类"""

    def __init__(self,name,color):
        self.__name = name
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color



class Car(Veicle):
    """汽车类"""

    def __init__(self, name, color,pasNum):
        super().__init__(name, color)
        self.__pasNum = pasNum

    def showInfo(self):
        print("Car's name:" + self.name)
        print("Car's color:" + self.color)
        print("Car's passengerNumber:" + self.__pasNum)


class Truck(Veicle):
    """卡车类"""

    def __init__(self, name, color,cc):
        super().__init__(name, color)
        self.__carryCapacity = cc

    def showInfo(self):
        print("Truck's name:" + self.name)
        print("Truck's color:" + self.color)
        print("Truck's carryCapacity:" + self.__carryCapacity)


car_in = input().split()
car = Car(*car_in)
truck_in = input().split()
truck = Truck(*truck_in)
car.showInfo()
truck.showInfo()




