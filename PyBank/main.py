import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")




month_count = 0

def revenue_row


with open(pybank_csv) as pybankcsv:
    pybankreader = csv.reader(pybankcsv, delimiter = ',')
    csv_header = next(pybankcsv)
    total_revenue = 0
    average_change = 0
    i = 1
    for row in pybankreader:
        month_count += 1
        total_revenue += int(row[1])
        if row[0]== "Revenue"
        
        #average_change = 

    



print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: ${total_revenue}")
#print(pybankreader)
#print(total_change)
#print(f"Average Change: {average_change}")


