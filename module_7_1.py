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
        try:
            with open(self.__file_name, 'r') as file:
                products = file.readlines()
            return [line.strip() for line in products]
        except FileNotFoundError:
            return []  # Если файл не найден, возвращаем пустой список

    def add(self, *products):
        existing_products = self.get_products()
        existing_product_names = [product.split(',')[0] for product in existing_products]

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_product_names:
                    file.write(f'{product}''\n')
                else:
                    print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # str
s1.add(p1, p2, p3)
print(s1.get_products())
