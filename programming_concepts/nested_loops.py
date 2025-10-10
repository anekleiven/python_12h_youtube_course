# nested loops = loop within loop 
# outer loop = 1st loop
#    inner loop = 2nd loop
# while loop inside for loop, for loop inside while loop, while loop inside while loop, for loop inside for loop etc. 

"""
for x in range(3): 
    for y in range(1,10): 
        print(y, end ="")
    print()
"""

rows = int(input("Enter the number of rows: ")) 
columns = int(input("Enter the number of columns: ")) 
symbol = input("Enter a symbol to use: ") 

for x in range(rows): 
    for y in range(columns): 
        print(symbol, end="") 
    print() # print new line after inner loop is done 
