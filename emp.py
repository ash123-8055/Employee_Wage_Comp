import random 

def attendance():
    random_checker=random.randint(0,1)
    if random_checker==1:
        print("The Employee is present")
    else:
        print("The Employee is absent")
    
print("Welcome to Employee Wage Computation")
attendance()
