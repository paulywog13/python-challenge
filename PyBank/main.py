import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

month_count = 0
revenue_changes = []
months = []

outputfile= os.path.join('Analysis', "Budget_Data.txt")
with open(pybank_csv) as pybankcsv:
    pybankreader = csv.reader(pybankcsv, delimiter = ',')
    csv_header = next(pybankcsv)
    total_revenue = 0
    average_change = 0
    previous_revenue = 867884
    for row in pybankreader:
        
        month_count += 1
        total_revenue += int(row[1])
        months.append(row[0])
        total_revenue_change = int(row[1])-previous_revenue
        revenue_changes.append(total_revenue_change)
        previous_revenue = int(row[1])
        greatest_increase = max(revenue_changes)
        greatest_decrease = min(revenue_changes)
                
    average_change = (round(sum(revenue_changes)/(len(revenue_changes)-1), 2))
    print(greatest_increase)
    print(greatest_decrease)
    max_month = months[revenue_changes.index(greatest_increase)]    
    min_month = months[revenue_changes.index(greatest_decrease)]
    


output =(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total months: {month_count}\n"
f"Total: ${total_revenue}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_month} (${greatest_increase})\n"
f"Greatest Increase in Profits: {min_month} (${greatest_decrease})\n"
)
print(output)

with open(outputfile, "w") as txt_file:
    txt_file.write(output)

