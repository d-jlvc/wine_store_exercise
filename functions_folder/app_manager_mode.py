#--This is a script dedicated to virtual manager:
#--importing store_manager.py and products_list.py:

from functions_folder.store_manager import StoreManager as Manager
from functions_folder import doc_functions as Doc
from functions_folder import products_list as Products

FILE_NAME = "products.txt" #--Changeable with option [7] - debug
Doc.create_new_txt(FILE_NAME)
Doc.load_from_txt(FILE_NAME)
#--MAIN PROGRAM
    
print("")
print(">>> 🧙‍♂️ - WELCOME TO MANAGER MODE! - 🧙‍♂️ <<<")
print(">>> 🆘 - Please, type 'help' for available commands!")

#--Instance and .txt load:
manager = Manager(Products.wine_list)




#--Looping through menu:
while True:
    
    user_input = input(">>>. Enter you command ('help' for commands): ")

    if user_input.lower() == 'help':
        print("""
            [1] - Add a new wine.
            [2] - Remove a wine from the list.
            [3] - Update wine stock.
            [4] - Update wine price.
            [5] - Check stock.
            [6] - Check complete wine list. 
            [7] - Change file name (create or edit another .txt).
            [Q] - Exit manager mode.
            """)
        
    elif user_input.upper() == 'Q':
        print("\n>>> 🧙‍♂️ - NOW EXITING MANAGER MODE...\n")
        import sys
        sys.exit()
    elif user_input == '1':
        manager.add_wine(FILE_NAME)
    elif user_input == '2':
        manager.remove_wine()
    elif user_input == '3':
        manager.update_stock()
    elif user_input == '4':
        manager.update_price()
    elif user_input == '5':
        manager.check_wine_stock()
    elif user_input == '6':
        manager.get_wine_list()
    # elif user_input == '7':
    #     Doc.change_filename(FILE_NAME) #--debug
    else:
        print(">>. Error! Type 'help' for command list!")
    