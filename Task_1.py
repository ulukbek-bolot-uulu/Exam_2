
class Country:

    def __init__(self, name, **kwargs):
        self.name = name
        print(self.name)
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])
            print("{} - {}".format(k, kwargs[k]))


country_1 = Country(name='USA', population='330 million', is_democratic=True)
country_2 = Country(name='Kyrgyzstan', area='200 km2', have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China'])

