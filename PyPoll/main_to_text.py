import os
import csv
Total = 0
khan_votes = 0
khan_p = 0
correy_votes = 0
correy_p = 0
li_votes = 0
li_p = 0
tooly_votes = 0
tooly_p = 0
w = 0
Winner = None
election_dataCSV = os.path.join('election_data.csv')
with open(election_dataCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
#     csv_first_row = next(csvfile)
    print(f"Header: {csv_header}")
    for row in csvreader:
        Total = Total + 1
        if (row[2] == "Khan"):
            khan_votes = khan_votes + 1
        if (row[2] == "Correy"):
            correy_votes = correy_votes + 1
        if (row[2] == "Li"):
            li_votes = li_votes + 1
        if(row[2] == "O'Tooley"):
            tooly_votes = tooly_votes + 1

        khan_p = format(round((khan_votes / Total) * 100.0 ,5) , '.3f')
        correy_p = format(round((correy_votes / Total ) * 100.0 ,5) , '.3f')
        li_p = format(round((li_votes / Total) * 100.0 , 5) , '.3f')
        tooly_p = format(round((tooly_votes / Total) * 100.0 ,5) , '.3f')
        w = max(khan_votes,correy_votes,li_votes,tooly_votes)
        if (w == khan_votes):Winner = "Khan"
        elif (w == correy_votes):Winner = "Correy"
        elif (w == li_votes):Winner = "Li"
        else:Winner = "O'Tooley"

    with open("Output.txt", "w") as text_file:
            print("Election Results",file=text_file)
            print("-------------------------",file=text_file)
            print(f"Total Votes :{Total}",file=text_file)
            print("-------------------------",file=text_file)
            print(f'Khan : {(khan_p)} { "(" + str(khan_votes) + ")" }',file=text_file)
            print(f'Correy : {correy_p} { "(" + str(correy_votes) + ")" }',file=text_file)
            print(f'Li : {li_p} { "(" + str(li_votes) + ")" }',file=text_file)
            print(f"O'Tooly : {tooly_p} { '(' + str(tooly_votes) + ')' }",file=text_file)
            print("-------------------------",file=text_file)
            print(f"Winner : {Winner}",file=text_file)
            print("-------------------------",file=text_file)

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes : {Total}")
    print("-------------------------")
    print(f'Khan : {(khan_p)} ({khan_votes})')
    print(f'Correy : {correy_p} ({correy_votes})')
    print(f'Li : {li_p} ({li_votes})')
    print(f"O'Tooly : {tooly_p} ({tooly_votes})")
    print("-------------------------")
    print(f"Winner : {Winner}")
    print("-------------------------")
