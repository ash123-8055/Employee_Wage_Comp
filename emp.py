import random 

def attendance():
    random_checker=random.randint(0,1)
    if random_checker==1:
        print("The Employee is present")
    else:
        print("The Employee is absent")

def wage_calculator():
    wage_per_hour=20
    full_day_hour=8
    part_time_hour=4
    daily_wage=wage_per_hour*full_day_hour
    part_time_wage=wage_per_hour*part_time_hour
    print("The daily wage of the employee is ", daily_wage)
    print("The part time wage of the employee is ", part_time_wage)

    
print("Welcome to Employee Wage Computation")
attendance()
wage_calculator()
