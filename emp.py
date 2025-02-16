import random 


def attendance():
    """Description: 
        This function uses random module to give attendance
       Parameter:
        None
       Return:
        Prints if the employee is present or absent"""

    random_checker=random.randint(0,1)
    if random_checker==1:
        print("The Employee is present")
    else:
        print("The Employee is absent")
    
print("Welcome to Employee Wage Computation")
attendance()
