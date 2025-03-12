#--This script simulates wine store

#--This class represents 'wine' object:
class Wine:
    
    def __init__(self, wine_id: int, wine_name: str, wine_type: str, wine_price: float, wine_quantity: int):
    #--This is where we create a 'wine' object, our number one product.
        self.wine_id = wine_id
        self.wine_name = wine_name
        self.wine_type = wine_type
        self.wine_price = wine_price
        self.wine_quantity = wine_quantity

#--Modules:
#------    
    def price_with_tax(self) -> float:
        """This module will return the price with an aditional tax (20%)."""
        return self.wine_price * 1.2 

#-----       
    def get_info(self) -> str:
        """This module will return the information about our product."""
        return f">.🍷 - ID:{self.wine_id} | '{self.wine_name}' | Type: {self.wine_type} | ${self.wine_price:.2f} | {self.wine_quantity}pcs."

#-----    
    def get_info_price(self) -> str:
        """This module will print wine price ('reduced info' for customer)."""
        return f">.🍷 - '{self.wine_name}' ({self.wine_quantity}pcs.) - ${self.price_with_tax():.2f}."

#-----    
    def get_info_stock(self) -> str:
        """This module checks the stock of our products."""
        if self.wine_quantity > 0:
            return f"'{self.wine_name}' is on stock!"
        else:
            return f"'{self.wine_name}' not on stock!"