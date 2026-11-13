from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product != None:
            self.__products.remove(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None
    
    def get_products(self) -> list[Product]:
        return list(self.__products)
    

    def display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-" * 48)
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def to_list(self) -> list[dict]:
        product_list = []
        for product in self.__products:
            product_list.append(product.to_dict())
        return product_list