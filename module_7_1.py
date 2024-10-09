
class Product:
    def __init__(self, name, weight=0.0, category=None):
        self.name = str(name)
        self.weight = weight
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.readlines()
        file.close()
        return products

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in products:
            if i.name not in [line.strip() for line in self.__file_name]:
                file.write(f'{i}''\n')
            else:
                print(f'Продукт {i} уже есть в магазине')
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
