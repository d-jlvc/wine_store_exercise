# wine_store_exercise
This is a repository containing an exercise simulating a wine store. 🛒🍾

❓ - Basically, this is me, a programming beginner, exercising python...
In this repository you can find a virtual wine store that you can access
either as a store manager (that let's you run the store) or as a customer
(buying wine etc..).

I've had an idea to store all the data in .txt file so that is an addition
which is kinda incomplete, but will be optimized, I just need to learn how. 😓

---------------------------------------------------------------------------

C O N T E N T:

📄 - main.py:
#--Here you'll find a main program from where you can run a simulation
(either as a 'manager' or 'customer')
📄 - products.txt:
#--A .txt document storing a list of wine. Unfortunately, it works only
when you add wine as a manager (which is incomplete, hopefully I'll complete
it and add .txt manipulation to every function)
📁 - functions_folder: stores scripts used for this program:
>>. - app_customer_mode.py - used in main.py for 'customer' simulation
>>. - app_manager_mode.py - used in main.py for 'manager' simulation
>>. - customer.py - stores 'class Customer' and all it's methods (used in app_customer_mode.py)
>>. - store_manager.py - stores 'class StoreManager' and all it's methods (used in app_manager_mode.py)
>>. - doc_functions.py - stores functions for manipulating .txt files
  (this part is incomplete, functions in this script are not placed everywhere,
  they are only in 'manager' simulation and are used only to create and append
  products.)
>>. - products_list.py - stores wine_list = {} and customer_cart = {}
  (This is where the items should've gone before I tried implementing
  .txt to store data. This works well I believe! 👐)
>>. - wine.py - store's 'class Wine' for creating Wine object.

❕❕ - PROBABLY BECAUSE OF THE IMPORTS - app_customer_mode.py and app_manager_mode.py won't run
themselves, B U T they run without an issue in main.py.

--------------------------------------------------------------------------

print("Stay safe! 🐍💻")
import sys
sys.exit()
