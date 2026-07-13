# Тебе нужно создать класс CurrencyConverter, который переводит рубли в доллары по определенному курсу.
#
# Задание: 1. Создай переменную класса usd_rate = 90.0 (это базовый курс).
# 2. Напиши метод convert_to_usd(self, rubles), который использует этот курс через self.
# 3. Создай два объекта: converter1 и converter2.
# 4. Сделай так, чтобы converter1 считал по базовому курсу (90.0), а для converter2 динамически измени курс внутри объекта на 95.0 (не меняя при этом базовый курс самого класса).

class CurrencyConverter:
    usd_rate = 90.0

    def converter_to_usd(self, roubles):
        return roubles / self.usd_rate

converter1 = CurrencyConverter()
converter2 = CurrencyConverter()
converter2.usd_rate = 95.0
print(converter1.converter_to_usd(900))
print(converter2.converter_to_usd(950))
