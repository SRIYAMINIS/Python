id=1001
basic_salary=15000
allowances=6000
gross_salary=basic_salary+allowances
if gross_salary>10000:
    income_tax=(gross_salary*20)/100
net_salary=gross_salary-income_tax
print("employee id:",id)
print("\nbasic_salary:",basic_salary)
print("\nallowances:",allowances)
print("\ngross_salary:",gross_salary)
print("\nincome_tax:",income_tax)
print("\nnet_salary:",net_salary)
