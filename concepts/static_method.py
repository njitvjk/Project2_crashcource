class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @staticmethod
    def is_electric(make):
        if make == 'Tesla':
            return True
        else:
            return False

    # instance method
    def check_car_variant(self):
        # call static method from instance method
        is_electric_flag = self.is_electric(self.make)
        print(f'Is {self.make} an electric variant:', is_electric_flag)


audi = Car('Audi', 'a4', 2019)
audi.check_car_variant()

ford = Car('Ford', 'eco sport', 2015)

tesla = Car('Tesla', 'model s', 2019)


# false
# because separate copy of instance method is created for each object
print(ford.check_car_variant() is audi.check_car_variant())

# True
# because only one copy is created
# ford and tesla objects share the same methods
print(ford.is_electric('Ford') is tesla.is_electric('tesla'))

# True
print(ford.is_electric('Ford') is audi.is_electric('Audi'))
