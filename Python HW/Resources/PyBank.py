#Worked closely with Dominic during Hackathon
# Dependencies
import csv
import os

# Files to load and output-change these
file_to_load = os.path.join('.','Resources','budget_data.csv')
file_to_output = os.path.join('budget_analysis.txt') 

#Define the variables 
months_total = 0
total_revenue_amount = 0
max_profit = 0
max_loss = 0
change = 0
greatest_inc = ["", 0]
greatest_dec = ["", 9999999999999999999]

list_revenue_change = []


# Read the csv file 
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

    header = next(reader)

    first_row = next(reader)
    months_total = months_total + 1
    total_revenue_amount = total_revenue_amount + int(first_row[1])
    prev_amt = int(first_row[1])

    for row in reader:   


        # Adding 1 to the total number of months for every row in the csv file
        months_total = months_total + 1

        # Adding revenue to the total revenue for every row in the csv file
        total_revenue_amount = total_revenue_amount + int(row[1]) 

        
        # Calculate the Average Revenue Change
        revenue_change = int(row[1]) - prev_amt
        prev_amt = int(row[1])
        print(revenue_change)
        list_revenue_change.append(revenue_change) 
        revenue_avg = sum(list_revenue_change) / len(list_revenue_change)

      
        

        # Find the biggest profit
      
        if revenue_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = revenue_change
        
        # Find the biggest loss
        if revenue_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = revenue_change



       

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total Revenue: ${total_revenue_amount}\n"
    f"Average Revenue Change: ${round(revenue_avg,2)}\n"
    f"Maximum Profit: {greatest_inc[0]} (${greatest_inc[1]})\n"
    f"Maximum Loss: {greatest_dec[0]} (${greatest_dec[1]})\n")
    #f"Significant Decrease in Revenue: {significant_decrease_rev[0]} (${significnat_decrease_rev[1]})\n")

# Print the output to terminal
 
print(output)

# Send the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)