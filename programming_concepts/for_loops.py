# for loops = used for iterating over a sequence (list, tuple, string) or other iterable objects 
#               iterating = going through elements one by one 
#               for <element> in <sequence>:
#                   <do something with element>


for x in reversed(range(1,11)): # 10-1
    print(x)
print("HAPPY NEW YEAR!")


credit_card = "1234-5678-9012-3456"

for x in credit_card: # iterate through each character in string
    print(x) 


for x in range(1,21): 
    if x == 13: 
        print("Unlucky number!")
        continue
    elif x == 15: 
        print("Skipping...")
        continue
    else: 
        print(x)