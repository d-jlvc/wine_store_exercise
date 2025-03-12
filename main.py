#--Main script / Running store as a manager or as a customer:

print("\n-- 🍾 W I N E  P A R A D I S E  S T O R E 🍾 --\n")
print("Would you like to access as 'manager' or as 'customer'?")
print("Use 'q' to exit!")

while True:

    user_input = input("Your selection: ")

    if user_input.lower() == 'manager':
        from functions_folder import app_manager_mode

    elif user_input.lower() == 'customer':
        from functions_folder import app_customer_mode
        
    elif user_input.lower() == 'q':
        print("\n-- 👋 G O O D  B Y E 👋--\n")
        import sys
        sys.exit()
    else:
        print("🚫 - Please select between 'manager' or 'customer'.")
        continue
    
