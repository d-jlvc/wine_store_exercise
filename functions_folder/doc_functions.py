#--This script contains functions for .txt and .json data:
#--Importing os for creating a new document:

import os
from functions_folder.wine import Wine


###
def save_to_txt(file_name, wine_list):
    """Saves wine products to .txt file."""
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write("ID | WINE NAME | WINE TYPE | WINE PRICE | WINE QUANTITY\n")    #--Initial line (legend)
        
        for wine_id, wine in wine_list.items():
            f.write(f"{wine_id} | {wine.wine_name} | {wine.wine_type} | {wine.wine_price:2f} | {wine.wine_quantity} \n")
            
    print(f">>>. 💾 - Files saved successfully to '{file_name}'.")
###    
def load_from_txt(file_name):
    """Loads information from .txt file"""
    
    wine_list = {} #--Stores wine objects
    max_id = 0 #--for generating new ID
    
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("ID |"):
                    continue
                
                wines = line.strip().split(" | ")
                
                if len(wines) != 5:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                
                try:
                    wine_id = int(wines[0])
                    wine_name = wines[1]
                    wine_type = wines[2]
                    wine_price = float(wines[3])
                    wine_quantity = int(wines[4])
                    
                    
                    wine = Wine(wine_id, wine_name, wine_type, wine_price, wine_quantity)
                    wine_list[wine_id] = wine
                    
                    if wine_id > max_id:
                        max_id = wine_id
                except ValueError as e:
                    print(f"Error processing line: {line.strip()} - {e}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found!")
    return wine_list, max_id
###
def create_new_txt(file_name):
    """Creates a new .txt file"""
    
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write("ID | WINE NAME | WINE TYPE | WINE PRICE | WINE QUANTITY\n")
        
        print(f"\n>>>. ✨ - '{file_name}' successfully created.\n")
    else:
        print(f"\n>>>. 👍 - '{file_name}' already exists.\n")

###
@staticmethod
def append_wine_to_txt(file_name, new_wine):
    with open(file_name, "r+", encoding="utf-8") as f:
        lines = f.readlines()

        # If wine exist
        for line in lines:
            if line.startswith(f"{new_wine.wine_id} |"):
                print(f">>>. ⚠ - Error! Wine with ID:{new_wine.wine_id} already exists and IS NOT ADDED TO .TXT FILE.")
                return

        # If wine doesn't exist
        f.write(f"{new_wine.wine_id} | {new_wine.wine_name} | {new_wine.wine_type} | {new_wine.wine_price} | {new_wine.wine_quantity}\n")
        print(f">>>. 🍷 - Wine '{new_wine.wine_name}' added to .txt.\n")
        
###
# def change_filename(file_name):
    
    
#     print(f"Current file name: {file_name}")
#     print("Change file name to save new or load other .txt files")
    
#     while True:
#         old_filename = input("Enter old filename (.txt): ")
#         new_filename = input("Enter new filename (.txt): ")
        
#         #old_filename = file_name
        
#         if old_filename == new_filename:
#             print("Error! Enter different file names: ")
#             continue
#         else:
#             new_filename = file_name
#             print(f"File name changed to: {new_filename}.")