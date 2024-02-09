import csv

#opens file and creates file object
infile = open('customers.csv', 'r')
csv_file =csv.reader(infile)
outfile = open('customer_country.csv', 'w', newline='')
total = 0

#csvfile = csv.writer(customers)
#create header
outfile.write('Full Name,Country\n')

#this will skip first record which is the header
next(csv_file)

for rec in csv_file:
    #parse row
    id_num = rec[0]
    first_name = rec[1]
    last_name = rec[2]
    city = rec[3]
    country = rec[4]
    total += 1
    
    outfile.write(f'{first_name} {last_name},{country}\n')
    
outfile.write(f'\nNumber of Customers: {total}') 
  
infile.close()
outfile.close()

