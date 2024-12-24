work_hours = [('Raj',400),('Rahul',3000),('Ramesh',200)]  # data that is going to be used

def employee_check(work_hours):  # function definition to find employee of the month

    current_max = 0  # initial value
    employee_of_the_month = ''  # initial value

    for employee,hours in work_hours:  # for loop
        if hours > current_max:  
            current_max = hours
            employee_of_the_month = employee 
        else:
            pass

    return (employee_of_the_month,current_max)  # return statement
result = (employee_check(work_hours))
print(result)
employee,hours = employee_check(work_hours)
print(employee)