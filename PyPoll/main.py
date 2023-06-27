import csv, os

# global variables
tot_votes = 0
CCS = "Charles Casper Stockham"
CCS_votes = 0
DD = "Diana DeGette"
DD_votes = 0
RAD = "Raymon Anthony Doane"
RAD_votes = 0
winner_name = ""

# open and alias data from election_data.csv
# alias path to data file
raw_poll_data = os.path.join("Resources", "election_data.csv")

with open(raw_poll_data) as raw_data:
    rw_poll = csv.reader(raw_data, delimiter=",")

    headers = next(rw_poll, None)

# create variable and track the total number of votes cast
    for row in rw_poll:
        # total
        tot_votes += 1
    # for each candidate
        if row[2] == CCS:
            CCS_votes += 1
        elif row[2] == RAD:
            RAD_votes += 1
        else:
            DD_votes += 1

# caluclate the percentage of votes each candidate reacevied

CCS_perc = CCS_votes / tot_votes
DD_perc = DD_votes / tot_votes
RAD_perc = RAD_votes / tot_votes

# determine the winner of the election
if CCS_votes > DD_votes and CCS_votes > RAD_votes:
    winner_name = CCS
elif DD_votes > CCS_votes and DD_votes > RAD_votes:
    winner_name = DD
else:
    winner_name = RAD

# report the Election Results to the terminal
# results list with lines of output
results = [
    "Election Results", 
    "---------------------------",
    f"Total Votes: {tot_votes}", 
    "---------------------------", 
    f"Charles Casper Stockham: {CCS_perc:.3%} ({CCS_votes})", 
    f"Diana DeGette: {DD_perc:.3%} ({DD_votes})",
    f"Raymon Anthony Doane: {RAD_perc:.3%} ({RAD_votes})",
    "---------------------------",
    f"Winner: {winner_name}",
    "---------------------------"
    ]

# print to terminal
for line in results:
    print(line + "\n")

# export the same results to a new text document
# alias output file
output_file = os.path.join("analysis", "pypoll_analysis.txt")

# write to new analysis txt file
with open(output_file, "a") as analysis:
    for line in results:
        analysis.write(line + "\n")