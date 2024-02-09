import csv

#initialize variables
efficient = True
total_forty = 0
total_thirty = 0
total_twenty = 0

#open file and create file object
employees = open('employee_data.csv', 'r')

csv_file = csv.reader(employees)



#skip header
next(csv_file)

#convert to list to reiterate
reader = list(csv_file)

#header
print('Highly Efficient Individuals:')

for rec in reader:
    #parse rows
    id_num = rec[0]
    name = rec[1]
    age = rec[2]
    salary = rec[3]
    hours = float(rec[4])
    productivity = float(rec[5])
    team = rec[6]
    bonus = rec[7]
    
    #calc efficiency
    efficiency = productivity / hours
    
    #determine efficient
    if efficiency > 2:
        efficient = True
    else:
        efficient = False
    
    if efficient:
        print(name)

print('\n')
#low efficiency header
print('Low Efficiency Individuals:')
#identify low efficient individuals
for rec in reader:
    #parse rows
    id_num = rec[0]
    name = rec[1]
    age = rec[2]
    salary = rec[3]
    hours = float(rec[4])
    productivity = float(rec[5])
    team = rec[6]
    bonus = rec[7]
    
    #calc efficiency
    efficiency = productivity / hours
    
    #determine efficiency
    if efficiency > 2:
        efficient = True
    elif efficiency < 2:
        efficient = False
    
    if not efficient:
        print(name)

#determine age groups  
print()      
print('Employees in their 40s')
for rec in reader:
    #parse rows
    id_num = rec[0]
    name = rec[1]
    age = int(rec[2])
    salary = rec[3]
    hours = float(rec[4])
    productivity = float(rec[5])
    team = rec[6]
    bonus = rec[7]
    
    if age >= 40:
        print(name)
        total_forty += 1

print()
print(f'Total number of employees in their 40s: {total_forty}')

print()
print('Employees in their 30s')
for rec in reader:
    #parse rows
    id_num = rec[0]
    name = rec[1]
    age = int(rec[2])
    salary = rec[3]
    hours = float(rec[4])
    productivity = float(rec[5])
    team = rec[6]
    bonus = rec[7]
    
    #identify age range
    if age >= 30 and age < 40:
        print(name)
        total_thirty += 1

print()
print(f'Total number of employees in their 30s: {total_thirty}')
print()

#identify employees in their 20s
print('Employees in their 20s')
for rec in reader:
    #parse rows
    id_num = rec[0]
    name = rec[1]
    age = int(rec[2])
    salary = rec[3]
    hours = float(rec[4])
    productivity = float(rec[5])
    team = rec[6]
    bonus = rec[7]
    
    #determine age range
    if age >= 20 and age <30:
        print(name)
        total_twenty += 1
        
print()
print(f'Total number of employees in their 20s: {total_twenty}')

