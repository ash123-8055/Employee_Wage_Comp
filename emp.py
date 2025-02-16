import random 


class Employee:
    def __init__(self,total_days,full_day_hour,part_time_hour,wage_per_hour):
        self.present=0
        self.absent=0
        self.total_days=total_days
        self.full_day_hour=full_day_hour
        self.part_time_hour=part_time_hour
        self.wage_per_hour=wage_per_hour
        self.total_hour=0
        self.daily_wage=0
        self.part_time_wage=0
        self.part_time=0
        self.full_time=0
    
    def attendance(self):
        """Description: 
            This function uses random module to give attendance
           Parameter:
            self: Object
           Return:
            Prints if the employee is present or absent"""

        for i in range(self.total_days):
            random_checker=random.randint(0,1)
            if random_checker==1:
                self.present+=1
            else:
                self.absent+=1

    def wage_calculator(self):
        """Description: 
            This function is used to calculate the wages of employee
           Parameter:
            self: object
           Return:
            Prints the daily wage and part time wage of employee"""

        for i in range(self.present):
            random_checker=random.randint(0,1)
            if random_checker==1:
                emp_type=1
            else:
                emp_type=2

            match emp_type:
                case 1:
                    self.full_day_hour=8
                    per_day_wage=0
                    per_day_wage=self.wage_per_hour*self.full_day_hour
                    self.daily_wage+=per_day_wage
                    self.full_time+=1
                case 2:
                    self.part_time_hour=4
                    per_day_wage=0
                    per_day_wage=self.wage_per_hour*self.part_time_hour
                    self.part_time_wage+=per_day_wage
                    self.part_time+=1
                case default:
                    pass

            self.total_hour=0        
            self.total_hour=(self.part_time*self.part_time_hour)+(self.full_time*self.full_day_hour)
            if self.total_hour>=100:
                print("Total working hours reached")
                break

        print(f"Total working days are {self.present+self.absent}")
        print(f"The number of days the employee was present is {self.present}")
        print(f"The number of days the employee was absent is {self.absent}")
        print(f"The number of days the employee worked full time is {self.full_time}")
        print(f"The number of days the employee worked part time is {self.part_time}")
        print(f"The monthly wage of the employee is {self.daily_wage+self.part_time_wage}")

total_days=int(input("Enter the total number of days: "))
full_day_hour=int(input("Enter the number of hours for full time: "))
part_time_hour=int(input("Enter the number of hours for part time: "))
wage_per_hour=int(input("Enter the wage per hour: "))
print("Welcome to Employee Wage Computation")
emp_one=Employee(total_days,full_day_hour,part_time_hour,wage_per_hour)
emp_one.attendance()
emp_one.wage_calculator()
