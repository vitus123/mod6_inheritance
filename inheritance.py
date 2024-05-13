class Car:
    price = 1000000

    def __str__(self):
        return  'Я {}, моя цена {}'.format(self.__class__.__name__,self.price)



    def horse_powers(self):
        print('Мощность: 500 л.с.')


class Nissan(Car):
    price = 750000

    def horse_powers(self):
        print('Мощность: 250 л.с.')


class KIA(Car):
    price = 550000

    def horse_powers(self):
        print('Мощность: 150 л.с.')


nissan = Nissan()
print(nissan)
nissan.horse_powers()
kia = KIA()
print(kia)
kia.horse_powers()