# WAP to get the basic salary from employee and
# calculate it gross salary (Basic salary + 10% DA and 12%TA)

def Calculate_Gross_Salary():
    basic_salary = input('Enter Basic salary of employee : ')
    da = basic_salary * 0.1
    ta = basic_salary * 0.12
    gross_salary = basic_salary + da + ta
    print('Gross salary of employee is = %r'%(gross_salary))



# Making call to above function

Calculate_Gross_Salary()
