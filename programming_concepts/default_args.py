# default arguments = a default value for certain parameters 
# makes functions more flexible and reduces number of arguments needed to call a function 


def net_price(list_price, discount=0, tax=0.05): 
    return list_price * (1 - discount) * (1 + tax)

print(net_price(1000)) # use default discount and tax 
print(net_price(1000, 0.1)) # use custom discount and default tax
print(net_price(1000, 0.1, 0.1)) # use custom discount and custom tax 

# count up timer 

import time 

def count(end, start=0): 
    for x in range(start,end+1): 
        print(x) 
        time.sleep(1) 
    print("Done!") 


count(30,15) 