# Python writing files (.txt, .json, .csv) 

# txt files

employees = ["Matt", "Jason", "Odd", "Lars", "Mia"]

file_path = "output.txt"

# file closes automatically because of 'with'
try: 
    with open(file = file_path, mode = "w") as file: 
        for employee in employees: 
            file.write(employee + " ") 
        print(f"txt file '{file_path}' was created") 
except FileExistsError: 
    print("That file already exists") 

# mode = 'w' writes a file (will overwrite a file) 
# mode = "x" only writes a file if it doesn't already exists 
# mode = "r" reads files 
# mode = "a" appending data to a file 



# JSON files 

import json 

file_path = "output.json"

employee = {
    "name": "Matt",
    "age": 29,
    "job": "Key account manager"
}

try: 
    with open(file_path, "w") as file: 
        json.dump(employee, file, indent=4) 
        print(f"json file '{file_path}' was created")
except FileExistsError: 
    print("That file already exists") 



# csv files 

import csv

employees = [["Name", "Age", "Job"],
             ["Lars", 80, "Doctor"],
             ["Matt", 45, "Dentist"],
             ["Mia", 25, "Bartender"]]

file_path = "output.csv" 

try:
    with open(file_path, "w", newline="") as file: 
        writer = csv.writer(file)
        for row in employees: 
            writer.writerow(row) 
        print(f"csv file '{file_path}' was created") 
except FileExistsError: 
    print("File already exists!") 
