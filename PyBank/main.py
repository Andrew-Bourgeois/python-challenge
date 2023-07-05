import csv
import os

# create variables to track specific details
row_count = 0
net_pl = 0
last_pl = 0
current_pl = 0
tot_avg = 0
largest_inc = 0
largest_inc_date = ""
largest_dec = 0
largest_dec_date = ""

#   There are two columns in raw data: "Date" and "Profit/Losses"
#   create a Python script which:
#   opens and pulls in the raw data
#   create path to raw data
raw_data_csv = os.path.join("Resources", "budget_data.csv")

with open(raw_data_csv) as raw_data:
    rw_data = csv.reader(raw_data, delimiter=",")

    # store header row
    headers = next(rw_data, None)

    # loop through remaining lines
    for row in rw_data: 
        #   increment the total number of months in the data set
        row_count += 1 
        #   Net total P&L over the entire period
        net_pl += float(row[1])
        #   The changes of profit and loss from period to period and the average of those changes
        current_pl = float(row[1]) - last_pl
        # track running total of monthly changes for avg after first row
        if row_count > 1:
            tot_avg += current_pl
        # update last profit and loss
        last_pl = float(row[1])
        #   The Greatest increase in profits (date and amount) over entire period
        if current_pl > largest_inc:
            largest_inc = current_pl
            largest_inc_date = row[0]
        #   greatest decrease in profit (date and amount)
        elif current_pl < largest_dec:
            largest_dec = current_pl
            largest_dec_date = row[0]


# print results by creating a list of result lines
results = []
# add print lines to results using .extend() and a tuple of results strings
results.extend(
    ("Financial Analysis", 
    "--------------------------", 
    f"Total Months: {row_count}", 
    f"Total: ${net_pl:.0f}", 
    f"Average Change: ${(tot_avg / (row_count - 1)):.2f}", 
    f"Greatest Increase in Profits: {largest_inc_date} (${largest_inc:.0f})", 
    f"Greatest Decrease in Profits: {largest_dec_date} (${largest_dec:.0f})")
    )

# print to terminal from results using for loop
print()
for line in results:
    print(line)

# create output file path
output_file = os.path.join("analysis", "pybank_analysis.txt")

# write results to the new txt ouput file
with open(output_file, "w") as analysis:
    for line in results:
        analysis.write(line + "\n")
