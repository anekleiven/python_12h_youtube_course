# Python reading files 
# .txt, .json, .csv 

# txt file: 

file_path = "output.txt" 

try:
    with open(file_path, mode = "r") as file: 
        content = file.read() 
        print(content) 
except FileNotFoundError:
    print("That file was not found") 
except PermissionError: 
    print("You do not have permission to read this file") 


# json file: 

import json 

file_path = "output.json" 

try: 
    with open(file_path, "r") as file: 
        content = json.load(file) 
        print(content["name"])                  # access the value of the key 'name' 
except FileNotFoundError: 
    print("That file was not found") 
except PermissionError: 
    print("You do not have permissioon to access this file") 



# csv file: 

import csv 

file_path = "output.csv" 

try: 
    with open(file_path, "r") as file: 
        content = csv.reader(file) 
        for line in content: 
            print(line[0])                      # read the first column in the csv file 
except FileNotFoundError: 
    print("That file was not found") 
except PermissionError: 
    print("You do NOT have permission to read this file.....") 






