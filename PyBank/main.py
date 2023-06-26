import csv
import os

# global variables to track specific details
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
#   * opens and pulls in the raw data
raw_data_csv = os.path.join("Resources", "budget_data.csv")

with open(raw_data_csv) as raw_data:
    rw_data = csv.reader(raw_data, delimiter=",")

    headers = next(rw_data, None)

    for row in rw_data: 
        #   * totals the number of months in the data set
        row_count += 1 
        #   * Net total P&L over the entire period
        net_pl += float(row[1])
        #   * The changes of profit and loss from period to period and the average of those changes
        current_pl = float(row[1]) - last_pl
        # track running total of monthly changes for avg after first row
        if row_count > 1:
            tot_avg += current_pl
        # update last profit and loss
        last_pl = float(row[1])
        #   * The Greatest increase in profits (date and amount) over entire period
        if current_pl > largest_inc:
            largest_inc = current_pl
            largest_inc_date = row[0]
        #   * greatest decrease in profit (date and amount)
        elif current_pl < largest_dec:
            largest_dec = current_pl
            largest_dec_date = row[0]


# (no longer used) print results to terminal using multi-line f-string
"""
Chose to optimize code using a tuple to iterate over for printing and writing to a text file. Original code for MVP (minimum viable product) looked like so, using a multi-line f-string:
"""
# print(f"""
# Financial Analysis
# ___________________________
# Total Months: {row_count}
# Total: ${net_pl: .0f}
# Average Change: ${(tot_avg / (row_count - 1)): .2f}
# Greatest Increase in Profits: {largest_inc_date}(${largest_inc: .0f})
# Greatest Decrease in Profits: {largest_dec_date}(${largest_dec: .0f})
# """)


# print results by creating a list of result lines
results = []
# add print lines to results using .extend() and a tuple of results strings
results.extend(
    ("Financial Analysis", 
    "___________________________", 
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

# create output file
output_file = os.path.join("analysis", "pybank_analysis.txt")

with open(output_file, "a") as analysis:
    for line in results:
        analysis.write(line + "\n")

    # (no longer used) write each line to analysis
    """
    Chose to optimize by using a list of lines and then a for loop to write to .txt file.
    """
    # analysis.write("Financial Analysis\n")
    # analysis.write("___________________________\n")
    # analysis.write(f"Total Months: {row_count}\n")
    # analysis.write(f"Total: ${net_pl:.0f}\n")
    # analysis.write(f"Average Change: ${(tot_avg / (row_count - 1)):.2f}\n")
    # analysis.write(f"Greatest Increase in Profits: {largest_inc_date} (${largest_inc:.0f})\n")
    #analysis.write(f"Greatest Decrease in Profits: {largest_dec_date} (${largest_dec:.0f})\n")


