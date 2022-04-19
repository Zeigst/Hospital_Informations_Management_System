class Medicine():
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = 0

    # Get Methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # Set Methods:
    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_stock(self, stock):
        self.__stock = stock