import csv
bonus = 0

#opens file and creates file object
employees = open('employee_data.csv', 'r')

csv_file = csv.reader(employees)

#this will skip first record which is the header
next(csv_file)

for rec in csv_file:
    #calc bonus and pay
    salary = float(rec[3])
    bonus_perc = float(rec[7])
    bonus = bonus_perc * salary
    total_pay = bonus + salary
    #print(rec) 
    print(f'Name: {rec[1]}')
    print(f'Salary: $  {salary:10,.2f}')
    print(f'Bonus:  $  {bonus:10,.2f}')
    print(f'Pay:    $  {total_pay:10,.2f}')
    
    input()
    