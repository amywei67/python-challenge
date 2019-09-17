import os
import csv

polls_by_candidates = {}

with open('election_data.csv') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    headerrow = next(reader)
    # print(headerrow)

    voter_tally = 0
    for row in reader:
        voter_tally += 1

        current_voter_id = row[0]
        current_candidate = row[2]

        if current_candidate not in polls_by_candidates:
            polls_by_candidates[current_candidate] = 0

        polls_by_candidates[current_candidate] += 1

print("Total Votes: {}".format(voter_tally))

winner = ""
highest_votes = 0
percentage_by_candidates = {}
for candidate in polls_by_candidates:
    votes = polls_by_candidates[candidate]
    percentage = float(votes) / voter_tally * 100
    percentage_by_candidates[candidate] = percentage

    # Format the float number to print 3 decimals
    print("{}: {:.3f}% ({})".format(candidate, percentage, votes))

    if votes > highest_votes:
        winner = candidate
        highest_votes = votes

print("Winner: "+winner)

output_file = "Python_HW_PyRoll_Output.txt"
with open(output_file, 'w') as filevariable:
    filevariable.write("--------------------------\n")
    filevariable.write("---  Election Results  ---\n")
    filevariable.write("--------------------------\n")
    filevariable.write("Total Votes: " + str(voter_tally))
    filevariable.write("\n--------------------------\n")

    for candidate in polls_by_candidates:
        filevariable.write("{}: {:.3f}% ({})\n".format(candidate, percentage_by_candidates[candidate], polls_by_candidates[candidate]))

    filevariable.write("--------------------------\n")
    filevariable.write("Winner: " + winner)
    filevariable.write("\n--------------------------\n")
