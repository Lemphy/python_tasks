class Vehicle:
    fuel_type = 'Бензин'

    def get_fuel_info(self):
        return f'Этот транспорт является {ElectricCar.fuel_type}'

class ElectricCar(Vehicle):
    fuel_type = 'Электричество'

object1 = Vehicle()
print(object1.get_fuel_info())