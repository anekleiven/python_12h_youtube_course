# multithreading = used to perform multiple tasks concurrently (multitasking) 
# good for I/O bound tasks like reading files or fetching data from API's (things that may take some time) 
# Thread(target = my_function) 

import threading 
import time

def walk_dog(first, last): 
    time.sleep(8) 
    print(f"You finish walking {first} {last}") 

def take_out_trash(): 
    time.sleep(2) 
    print("You take out the trash") 

def get_mail():
    time.sleep(4) 
    print("You get the mail from the mail box") 

# use threads to run functions simultaneously 

chore1 = threading.Thread(target = walk_dog, args = ("Molly", "Boo"))  
chore1.start() 

chore2 = threading.Thread(target=take_out_trash) 
chore2.start() 

chore3 = threading.Thread(target=get_mail)
chore3.start() 

# with the join method, you will wait with printing the 'complete message' until the chores are complete 

chore1.join()
chore2.join()
chore3.join() 


print("-" * 60)
print("All chores are complete 🎉") 
print("-" * 60)
