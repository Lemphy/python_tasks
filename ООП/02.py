class Vehicle:
    fuel_type = 'Бензин'

    def get_fuel_info(self):
        return f'Этот транспорт является {self.fuel_type}'

class ElectricCar(Vehicle):
    fuel_type = 'Электричество'

object1 = ElectricCar()
print(object1.get_fuel_info())