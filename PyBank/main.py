# Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join('.',  'Resources', 'budget_data.csv')

# Read the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Variables
    total_months = 0
    net_amount = 0
    monthly_change = []
    month_count = []
    greatest_increase = 0
    greatest_increase_month = 0
    greatest_decrease = 0
    greatest_decrease_month = 0
  
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Loop through all the rows
    for row in csvreader:
        
        total_months += 1
        net_amount += int(row[1])


        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        

        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
    
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print to Terminal
print(f"Financial Analysis")
print(f"----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")

# Specify the file to write to
output_file = os.path.join('.', 'budget_data')

with open("results.txt","w+") as txt_file:

    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_amount}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")