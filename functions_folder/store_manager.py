#--This class represents 'manager' of the store:
#--Importing wine.py for object creation:

from functions_folder.wine import Wine
from functions_folder import doc_functions as Doc

class StoreManager:
#-----
    def __init__(self, wine_list=None):
    #--Connecting to products.py
        self.wine_list = wine_list if wine_list else {}

#--Modules:        

    def get_wine_list(self):
        """This module prints out wine list."""
        for wine in self.wine_list.values():
            #--get_info() from class Wine:
            print(wine.get_info())
            
#-----
    def check_wine_stock(self):
        """This module lets manager track the wine stock."""
        for wine in self.wine_list.values():
            if wine.wine_quantity > 5:
                print(f">. 👍 - ID:{wine.wine_id} '{wine.wine_name}' stock: {wine.wine_quantity}. STOCK OK!")
            if wine.wine_quantity > 0 and wine.wine_quantity <5:
                print(f">. 🤏 - ID:{wine.wine_id} '{wine.wine_name}' stock: {wine.wine_quantity}. CONSIDER RESTOCKING!")
            if wine.wine_quantity <= 0:
                print(f">. 👏 - ID:{wine.wine_id} '{wine.wine_name}' OUT OF STOCK!")

#-----
    def get_reduced_stock(self): #--used in def update_wine()
        """This module will print only ID, name and quantity of wine (for 'manager' update)."""
        print(f"\n>. 📥 - Stock update mode:")
        print("")
        for wine in self.wine_list.values():
            print(f">. 🍷 - ID:{wine.wine_id} '{wine.wine_name}' | {wine.wine_quantity}pcs.")
                
#-----
    def get_deletion_stock(self): #--used in def remove_wine()
        """This module will print only ID, name and quantity of wine (for 'manager' deletion)."""
        print(f"\n>. ❌ - Wine deletion mode:")
        print("")
        for wine in self.wine_list.values():
            print(f">. 🍷 - ID:{wine.wine_id} '{wine.wine_name}' | {wine.wine_quantity}pcs.")

#------            
    def get_price_stock(self): #--used in def update_price()
        """This module will print only ID, name and price of wine (for 'manager' price update)."""
        print(f"\n>. 💲 - Price update mode:")
        print("")
        for wine in self.wine_list.values():
            print(f">. 🍷 - ID:{wine.wine_id} '{wine.wine_name}' | ${wine.wine_price}.")
            
                        
#-----                 
    def add_wine(self, file_name):
        """This module is for adding wines to wine list."""
        #--Inputs:
        while True:
            
            print("\n>. 🔤 - Type: [add] to add wine, [q] to exit.")
            user_input = input(">. Enter your choice: ")
            
            if user_input.lower() == 'add':
                
            #--ID CHECK FOR .TXT
                existing_id = set()
                with open(file_name, 'r', encoding='utf-8') as f:
                    for line in f.readlines()[1:]:
                        parts = line.strip().split(" | ")
                        if parts and parts[0].isdigit():
                            existing_id.add(int(parts[0]))
                            
            #--Loop for ID checking:
                while True:
                    
                    print("\n>. 💡 -  Type 'exit' to stop mid wine adding process.\n")
                    wine_id = input(">. Enter new ID for new wine: ")
                    
                    if wine_id.lower() == 'exit': #--for leaving input menu
                        print("\n>>. x - Exiting wine add function...")
                        print(">>. 🔙 - Returning to 'MANAGER MODE'...\n")
                        return
                    
                    if not wine_id.isdigit():
                        print(">. ⚠ - Error! Please use numerical values!")
                    else:
                        wine_id = int(wine_id)
                        #--.txt id check
                        if wine_id in existing_id:
                            print(f">. ⚠ - Error! Wine with ID:{wine_id} already exists! Try another ID.")
                            continue
                            
                        if wine_id in self.wine_list:
                            print(f">. ⚠ - Error! ID:{wine_id} already in use! Please select a new one!")
                            continue
                        
                        break
                    
            #--Loop for name checking:    
                while True:
                        
                    wine_name = input(">. Enter name of new wine: ")
                    
                    if wine_name.lower() == 'exit': #--for leaving input menu
                        print("\n>>. x - Exiting wine add function...")
                        print(">>. 🔙 - Returning to 'MANAGER MODE'...\n")
                        return
                    
                    if any(wine.wine_name == wine_name for wine in self.wine_list.values()):
                        print(f">. ⚠ - '{wine_name}' already on stock! Consider using 'Stock update'!")
                    else:
                        break
                    
                wine_type = input(">. Enter type of new wine: ")
                
                if wine_type.lower() == 'exit': #--for leaving input menu
                    print("\n>>. x - Exiting wine add function...")
                    print(">>. 🔙 - Returning to 'MANAGER MODE'...\n")
                    return
                
                #--Loop for price checking:
                while True:
                    
                    wine_price = input(">. Enter price of new wine: ")
                    
                    if wine_price.lower() == 'exit': #--for leaving input menu
                        print("\n>>. x - Exiting wine add function...")
                        print(">>. 🔙 - Returning to 'MANAGER MODE'...\n")
                        return
                    
                    try:
                        wine_price = float(wine_price)
                        break
                    except ValueError:
                        print(">. ⚠ - Error! Please enter a valid numerical value!")
                        continue #--restart the loop if input is invalid
                    
                #--Loop for quantity checking:    
                while True:
                        
                    wine_quantity = input(">. Enter the quantity of new wine: ")
                    
                    if wine_quantity.lower() == 'exit': #--for leaving input menu
                        print("\n>>. x - Exiting wine add function...")
                        print(">>. 🔙 - Returning to 'MANAGER MODE'...\n")
                        return
                    
                    if not wine_quantity.isdigit():
                        print(">. ⚠ - Error! Please use numerical values!")
                    else:
                        wine_quantity = int(wine_quantity)
                        break 

                #--Creating a new wine:
                new_wine = Wine(wine_id, wine_name, wine_type, wine_price, wine_quantity)
                
                #--Adding a new wine to dictionary:
                self.wine_list[wine_id] = new_wine
                
                #--Message:
                print(f"\n>. ✅ - '{wine_name}' added to stock!")
                
                #--.txt append:
                Doc.append_wine_to_txt(file_name, new_wine)
                
            elif user_input.lower() == 'q':
                print(">. 👋 - Bye!")
                break
            else:
                print(">. ⚠ - Unknown input! Please, use 'add' or 'q' as described.")               

#-----
    def update_stock(self):
        """This module will allow manager to update the stock:"""
        #--Inputs:
        while True:
            
            print("\n>. 📥 - Type: [upd] to update stock, [q] to exit.")
            user_input = input(">. Enter your choice: ")
            
            if user_input.lower() == 'upd':
                
                print("") #--empty row
                print(self.get_reduced_stock())
                
                #--Loop for ID checking:
                while True:
                    
                    wine_id = input(">. Enter the product ID that needs restocking: ")
                    
                    if not wine_id.isdigit():
                        print(">. ⚠ - Error! Please use numerical values!")
                    else:
                        wine_id = int(wine_id)
                        
                        if wine_id not in self.wine_list:
                            print(f">. ⚠ - Error! ID:{wine_id} not found!")
                        else:
                            break
                
                #--Loop for stock checking:
                while True:
                    
                    new_stock = input(">. Enter new stock: ")
                    
                    if not new_stock.isdigit():
                        print(">. ⚠ - Error! Please use numerical values!")
                    else:
                        new_stock = int(new_stock)
                        
                        #--Creating variable for old stock:
                        current_stock = self.wine_list[wine_id].wine_quantity
                        
                        if new_stock == current_stock:
                            print(">. ⚠ - Error! You've entered the same value!")
                        else:
                            self.wine_list[wine_id].wine_quantity = new_stock
                            print(f">. ✅ - Stock updated! New stock of '{self.wine_list[wine_id].wine_name}' - {new_stock}pcs.")
                            break
                        
            elif user_input.lower() == 'q':
                print(">. 👋 - Bye!")
                break
            else:
                print(">. ⚠ - Unknown input! Please, use 'upd' or 'q' as described.")

#-----
    def update_price(self):
        """This module will allow manager to update the price of wine"""
        #--Inputs:
        while True:
            
            print("\n>. 💲 - Type: [prc] to update price, [q] to exit.")
            user_input = input(">. Enter your choice: ")
            
            if user_input.lower() == 'prc':
                
                print("") #--empty row
                print(self.get_price_stock())
             
                #--Loop for ID check:   
                while True:
                    
                    wine_id = input(">. Enter the product ID for price change: ")
                        
                    if not wine_id.isdigit():
                        print(">. ⚠ - Error! Please use numerical values!")
                    else:
                        wine_id = int(wine_id)
                        
                        if wine_id not in self.wine_list:
                            print(f">. ⚠ - Error! ID:{wine_id} not found!")
                        else:
                            break
                    
                #--Loop for stock checking:
                while True:
                    
                    new_price = input(">. Enter new price: ")
                    
                    try:
                        new_price = float(new_price)
                    except ValueError:
                        print(">. ⚠ - Error! Please enter a valid numerical value!")
                        continue #--restart the loop if input is invalid
                                          
                    #--Fetching current price from Wine object:
                    current_price = self.wine_list[wine_id].wine_price
                    
                    if new_price == current_price:
                        print(">. ⚠ - Error! You've entered the same value!")
                    else:
                        self.wine_list[wine_id].wine_price = new_price
                        print(f">. ✅ - Price updated! New price of '{self.wine_list[wine_id].wine_name}' - ${new_price}.")
                        break
            
            elif user_input.lower() == 'q':
                print(">. 👋 - Bye!")
                break
            else:
                print(">. ⚠ - Unknown input! Please, use 'upd' or 'q' as described.")

#-----                
    def remove_wine(self):
        """This module will allow manager to remove item from stock."""
        #--Inputs:
        while True:
                
            print("\n>. 📤 - Type: [del] to remove stock, [q] to exit.")
            user_input = input(">. Enter your choice: ")
        
            if user_input == 'del':
                
                print("") #--empty row
                print(self.get_deletion_stock())
                
                #--Loop for ID checking:
                while True:
                    
                    wine_id = input(">. Enter the product ID you wish to delete: ")
                
                    if not wine_id.isdigit():
                        print(">. ⚠ - Error! Please use numerical values!")
                    else:
                        wine_id = int(wine_id)
                            
                        if wine_id not in self.wine_list:
                            print(f">. ⚠ - Error! ID:{wine_id} not found!")
                        else:
                        
                            while True:
                                
                                backup_choice = input(">. Are you sure? [Y/N]: ")
                                
                                if backup_choice.upper() == 'Y':
                                    print(f">. ❎ - '{self.wine_list[wine_id].wine_name}' removed from stock.")
                                    del self.wine_list[wine_id]
                                    break #--Deletes the wine and returns to main menu
                                elif backup_choice.upper() == 'N':
                                    break #--Returns to main menu
                                else:
                                    print(">. ⚠ - Error! Please consider typing [Y] or [N].")
                            break
                        
            elif user_input == 'q':
                print(">. 👋 - Bye!")
                break
            else:
                print(">. ⚠ - Unknown input! Please, use 'del' or 'q' as described.")
