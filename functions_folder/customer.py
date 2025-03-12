#--This class represents 'customer:

class Customer:
#-----
    def __init__(self, wine_list=None):
        self.wine_list = wine_list if wine_list else {}
        self.customer_cart = {}
        
#--Modules:

    def get_customer_list(self): 
        """This module returns the price with 20% tax."""
        for wine in self.wine_list.values():
            print(wine.get_info_price())

#-----
    def view_cart(self):
        """This module returns the items in cart."""
            
        print(">>. 🛒 - Your cart:\n" + "-" * 50)
        for wine_name, quantity in self.customer_cart.items():
            #selected_wine = self.wine_list.get(wine_name)
            #if selected_wine:
            print(f">>. 🍾 - '{wine_name}' ({quantity}pcs.)")
            
        if not self.customer_cart:
            print(">>. 🚫 - Your cart is empty.\n")
                   
#-----
    def add_to_cart(self):
        
        while True: #--Customer choice:
            
            print("\n>. 🛒 - You are now adding items to cart! Type 'q' to exit.\n")
            print(">. 🍾 - WINE SELECTION: ")
            print("-" * 50)
            print(self.get_customer_list())
            print("-" * 50)
            
            user_input = input(">>. Which products would you like to add to cart? ")
            
            if user_input.lower() == 'q':
                print("\n>>. Returning to main menu...")
                break
            
            selected_wine = None
            for wine in self.wine_list.values():
                if wine.wine_name.lower() == user_input.lower():
                    selected_wine = wine
                    break
                
            if not selected_wine:
                print(f">>. ⚠ - Oops! '{user_input}' is not on our list... Please try again, or type 'q' to leave.")
                continue
            
            while True: #--Quantity check:
                
                quantity = input(">>. How much would you like to add? ")
                
                if quantity == 'q':
                    print("\n>>. Returning to main menu...")
                    break
                
                if not quantity.isdigit():
                    print(">>. ⚠ - Sorry, please type numerical values (e.g. '10').")
                else:    
                    quantity = int(quantity)
                    
                    if quantity > selected_wine.wine_quantity:
                        print(">>. ⚠ - Sorry! Not enough wine on stock... Please reconsider selection or type 'q' to leave.")
                        break
                    
                    self.customer_cart[selected_wine.wine_name] = self.customer_cart.get(selected_wine.wine_name, 0) + quantity
                    selected_wine.wine_quantity -= quantity
                    
                    print(f">>. 🎉 - '{selected_wine.wine_name}' ({quantity}pcs.) added to cart!")
                    break

#-----
    def remove_from_cart(self):
        """This module will allow customer to remove items from cart."""
        
        while True:
            
            print("\n>. 📤 - You are now removing items from cart! Type 'q' to exit.\n")
            print(self.view_cart())
            print("-" * 50)
            
                
            user_input = input(">>. Which products would you like to remove? ")
            
            if user_input.lower() == 'q':
                print("\n>>. Returning to main menu...")
                break
            
            selected_wine = None #--Variable for wine selection
            
            for wine in self.customer_cart:
                if wine.lower() == user_input.lower():
                    selected_wine = wine
                    break
                
            if not selected_wine:
                print(f">>. '{user_input}' not in your cart. Please, try again.")
                continue
            
            confirmation = input("Are you sure? [Y/N]: ")
            
            if confirmation.lower() == 'y':
                quantity_to_return = self.customer_cart[selected_wine]
                del self.customer_cart[selected_wine]
                
                for wine in self.wine_list.values():
                    if wine.wine_name == selected_wine:
                        wine.wine_quantity += quantity_to_return
                print(f">>. ✅ - '{selected_wine}' successfuly removed!")
            elif confirmation.lower() == 'n':
                print(">>. Deletion canceled... Returning item to cart...")
                break
            else:
                print(">>. ⚠ - Oops! Wrong input! Please, try again (Y or N).")
                continue

#-----            
    def search_by_type(self):
        """This module allows customer to search wines using their type."""
        
        while True:
            
            print("\n>. 🔍 - Welcome to our search engine. Type 'q' to exit.\n")
            print(">. 🍾 - Our selection offers 'Red', 'White' and 'Sparkling' types of wine!")
            
            user_input = input(">>. Enter the type of wine you wish to see: ")
            print("")
            
            if user_input.lower() == 'red':
                found_wine = False
                for wine in self.wine_list.values():
                    if wine.wine_type.lower() == "red":
                        found_wine = True
                        print(f">>. 🍷 - Our selection: {wine.wine_name} ({wine.wine_quantity}) - ${wine.price_with_tax()}.")
                    if not found_wine:
                        print(f">>. 😞 - Sorry, we have no {user_input} wines at this moment.")
                        
            elif user_input.lower() == 'white':
                found_wine = False
                for wine in self.wine_list.values():
                    if wine.wine_type.lower() == "white":
                        found_wine = True
                        print(f">>. 🍷 - Our selection: {wine.wine_name} ({wine.wine_quantity}) - ${wine.price_with_tax()}.")   
                    if not found_wine:
                        print(f">>. 😞 - Sorry, we have no {user_input} wines at this moment.")
                        
            elif user_input.lower() == 'sparkling':
                found_wine = False
                for wine in self.wine_list.values():
                    if wine.wine_type.lower() == "sparkling":
                        found_wine = True
                        print(f">>. 🍷 - Our selection: {wine.wine_name} ({wine.wine_quantity}) - ${wine.price_with_tax()}.")
                if not found_wine:
                    print(f">>. 😞 - Sorry, we have no {user_input} wines at this moment.")
                    
            elif user_input.lower() == 'q':
                print("\n>>. Exiting search engine...\n")
                break
            else:
                print(">>. ⚠ - Sorry! Only red, white or sparkling wines are available! Please try again.")
                continue
                
#-----           
    def price_filter(self):
        """This module allows customer to set price filter (min - max)."""
        
        print("\n>. 🔍 - Welcome to our search engine. Type 'q' to exit.")
        print(">. 💸 - This is our price filter.\n")
        
        while True:
            
            lowest_price = input(">>. Enter lowest price: ")
            
            if lowest_price == 'q':
                print(">>. Exiting price filter...")
                break
            
            try:
                lowest_price = float(lowest_price)
            except ValueError:
                print(">>. ⚠ - Oops! Please enter a valid numerical input.")
                continue
            
            if lowest_price < 0:
                print(">>. ⚠ - Oops! Please enter a valid numerical input.")
                continue
            
            while True:
            
                highest_price = input(">>. Enter highest price: ")
            
                if highest_price == 'q':
                    print(">>. Exiting price filter...")
                    break
            
                try:
                    highest_price = float(highest_price)
                except ValueError:
                    print(">>. ⚠ - Oops! Please enter a valid numerical input.")
                    continue
            
                if highest_price < lowest_price:
                    print(">>. ⚠ - Highest price cannot be lower than the lowest price. Please reconsider your inputs.")
                    continue
                
                break #--breaking out of nested loop for highest_price check
            
            found = False
            for wine in self.wine_list.values():
                if lowest_price <= wine.price_with_tax() <= highest_price:
                    found = True
                    print(f">>. 🍷 - '{wine.wine_name}' {wine.wine_type} - ${wine.price_with_tax()}")
                    
            if not found:
                print(">>. 😞 - Sorry! No wines in this price range.")
            
            while True:        
                exit_input = input(">>. Would you like to try again [Y/N]? ")
                if exit_input.lower() == 'n':
                    print("\n>>. Exiting price filter...")
                    break
                elif exit_input.lower() == 'y':
                    break
                else:
                    print(">>. ⚠ - Oops! Please enter 'y' or 'n'.")
                    
            if exit_input.lower() == 'n':
                break

#-----        
    def get_reciept(self):
        """This module prints the receipt."""
        
        print("\n>>> 🧾 - RECEIPT - 🧾 <<<")
        print("-" * 50)
        
        total_price = 0
        
        for wine_name, quantity in self.customer_cart.items():
            selected_wine = None
            
            for wine in self.wine_list.values():
                if wine.wine_name.lower() == wine_name.lower():
                    selected_wine = wine
                    break
            
            if selected_wine:
                price_with_tax = selected_wine.price_with_tax()
                wine_total_price = price_with_tax * quantity
                total_price += wine_total_price
                
                print(f">>. 🍷 - '{wine_name}' ({quantity} pcs) - ${price_with_tax} each")
                print(f">> Total for this wine: ${wine_total_price:.2f}")
                print("-" * 50)
                    
        print(f"\n>>> TOTAL COST: ${total_price:.2f}")
        print("-" * 50)