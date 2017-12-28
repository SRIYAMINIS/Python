basic_salary=15000
employee_id=1001
allowances=6000
gross_salary=basic_salary+allowances
if gross_salary<=5000:
    income_tax="nil"
elif gross_salary>5001 and gross_salary<=10000:
    income_tax=(gross_salary*10)/100
elif gross_salary>10001 and gross_salary<=20000:
    income_tax=(gross_salary*20)/100
else:
    income_tax=(gross_salary*30)/100 
net_salary=gross_salary-income_tax
print("employee id:",employee_id)
print("\nbasic_salary:",basic_salary)
print("\nallowances:",allowances)
print("\ngross_salary:",gross_salary)
print("\nincome_tax:",income_tax)
print("\nnet_salary:",net_salary)
