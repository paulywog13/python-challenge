import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

month_count = 0
revenue_changes = []

with open(pybank_csv) as pybankcsv:
    pybankreader = csv.reader(pybankcsv, delimiter = ',')
    csv_header = next(pybankcsv)
    total_revenue = 0
    average_change = 0
    previous_revenue = 867884
    for row in pybankreader:
        month_count += 1
        total_revenue += int(row[1])
        total_revenue_change = int(row[1])-previous_revenue
        revenue_changes.append(total_revenue_change)
        previous_revenue = int(row[1])
    print(sum(revenue_changes)/len(revenue_changes))
         

    



print("Financial Analysis")
print("----------------------------")
print(f"Total months: {month_count}")
print(f"Total: ${total_revenue}")
#print(pybankreader)
#print(total_revenue_change)
#print(f"Average Change: {average_change}")


