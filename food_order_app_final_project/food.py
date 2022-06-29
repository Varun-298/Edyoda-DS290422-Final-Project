class food:

    def __init__(self,food_id,food_name,food_quantity,food_price,discount,stock):
        self.food_id = food_id
        self.food_name = food_name
        self.food_quantity = food_quantity
        self.food_price = food_price
        self.discount = discount
        self.stock = stock

    def __str__(self):
         return f"Food ID : {self.food_id} \nFood Name : {self.food_name} \nFood Quantity : {self.food_quantity} \nFood Price : {self.food_price} \nDiscount : {self.discount} \nStock : {self.stock}"
    
    def set_food_id(self,food_id):
        self.food_id = food_id

    def get_food_id(self):
        return self.food_id
    
    def set_food_name(self,food_name):
        self.food_name = food_name

    def get_food_name(self):
        return self.food_name
    
    def set_food_quantity(self,food_quantity):
        self.food_quantity = food_quantity

    def get_food_quantity(self):
        return self.food_quantity
    
    def set_food_price(self,food_price):
        self.food_price = food_price

    def get_food_price(self):
        return self.food_price

    def set_discount(self,discount):
        self.discount = discount

    def get_discount(self):
        return self.discount

    def set_stock(self,stock):
        self.discount = stock

    def get_stock(self):
        return self.stock