class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def get_supplier_id(self) -> str:
        return self.__supplier_id

    def display_information(self) -> None:
        print(f"Supplier: {self.__name} ({self.__supplier_id}) | Email: {self.__contact_email}")