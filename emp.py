import random 

def attendance():
    global present
    global absent
    present=0
    absent=0
    total_days=20
    for i in range(total_days):
        random_checker=random.randint(0,1)
        if random_checker==1:
            present+=1
        else:
            absent+=1

def wage_calculator():
    global full_day_hour
    global part_time_hour
    global total_hour
    full_day_hour=0
    daily_wage=0
    part_time_wage=0
    part_time=0
    full_time=0
    for i in range(present):
        random_checker=random.randint(0,1)
        if random_checker==1:
            emp_type=1
        else:
            emp_type=2

        match emp_type:
            case 1:
                wage_per_hour=20
                full_day_hour=8
                per_day_wage=0
                per_day_wage=wage_per_hour*full_day_hour
                daily_wage+=per_day_wage
                full_time+=1
            case 2:
                wage_per_hour=20
                part_time_hour=4
                per_day_wage=0
                per_day_wage=wage_per_hour*part_time_hour
                part_time_wage+=per_day_wage
                part_time+=1
            case default:
                pass

        total_hour=0        
        total_hour=(part_time*part_time_hour)+(full_time*full_day_hour)
        if total_hour>=100:
            print("Total working hours reached")
            break

    print(f"Total working days are {present+absent}")
    print(f"The number of days the employee was present is {present}")
    print(f"The number of days the employee was absent is {absent}")
    print(f"The number of days the employee worked full time is {full_time}")
    print(f"The number of days the employee worked part time is {part_time}")
    print(f"The monthly wage of the employee is {daily_wage+part_time_wage}")
    
print("Welcome to Employee Wage Computation")
attendance()
wage_calculator()
