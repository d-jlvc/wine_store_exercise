#--This is a script dedicated to virtual customer:
#--importing store_manager.py and products_list.py:

from functions_folder import customer as Customer
from functions_folder import products_list as Products

        
#--MAIN PROGRAM
    
print("")
print(">>> 🛒 - WELCOME TO CUSTOMER MODE! - 🛒 <<<")
print(">>> 🆘 - Please, type 'help' for available commands!")

#--Instance:
customer_instance = Customer.Customer(Products.wine_list)

#--Looping through menu:
while True:
    
    user_input = input(">>>. Enter you command ('help' for commands): ")

    if user_input.lower() == 'help':
        print("""
            [1] - Add to cart.
            [2] - Remove from cart.
            [3] - View cart.
            [4] - Search by wine type.
            [5] - Price filter.
            [6] - Get receipt.
            [Q] - Exit customer mode.
            """)
        
    elif user_input.upper() == 'Q':
        print("\n>>> 🛒 - NOW EXITING CUSTOMER MODE...\n")
        import sys
        sys.exit()
    elif user_input == '1':
        customer_instance.add_to_cart()
    elif user_input == '2':
        customer_instance.remove_from_cart() #--needs fix
    elif user_input == '3':
        customer_instance.view_cart() #--needs fix
    elif user_input == '4':
        customer_instance.search_by_type() #--needs fix
    elif user_input == '5':
        customer_instance.price_filter() #--needs fix
    elif user_input == '6':
        customer_instance.get_reciept()
    else:
        print(">>. Error! Type 'help' for command list!")
    