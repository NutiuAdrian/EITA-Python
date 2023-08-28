salary = float(input('Please enter your salary: '))
#print(type(salary))
print(f'You have entered the salary of: {salary}')

tax = 0
#net_salary = 0

tax = tax + (salary * 0.25) # pension
tax = tax + (salary * 0.1) # healthcare

tax = tax + ((salary-tax) * 0.1) # 10% tax on revenue

net_salary = salary - tax

print(f'With a base salary of {salary}, you pay {tax} taxes and you are left with {net_salary}.')





