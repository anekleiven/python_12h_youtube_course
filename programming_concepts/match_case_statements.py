# match-case statement (switches in other programming languages): An alternative to using many elif statements 
# Execute some code in a value matches a case 
# Benefits: cleaner and syntax is more readable 


# classic way using if-elif-else 

def day_of_week(day): 
    if day == 1: 
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else: 
        return "{day} is not a valid day" 
    
print(day_of_week(1)) 

# using match-case statement 

def day_of_week(day): 
    match day: 
        case 1: 
            return "Monday"
        case 2:
            return "Tuesday"    
        case 3:
            return "Wednesday"  
        case 4:
            return "Thursday"
        case 5:
            return "Friday" 
        case 6: 
            return "Saturday"
        case 7:
            return "Sunday"
        case _:  # default case if no other case matches
            return f"{day} is not a valid day"
        
    print(day_of_week(3))


def is_weekend(day): 
    match day: 
        case "Sunday" | "Saturday": 
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":  # multiple options in one case
            return False
        case _: 
            return False  # default case 
            
print(is_weekend("Monday"))

