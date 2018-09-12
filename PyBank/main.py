import os
import csv
budget_dataCSV = os.path.join('budget_data.csv')
with open(budget_dataCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #csv_header = next(csvfile)
    next(csvreader)
    Total = []
    date = []
    Total_change = []
    for row in csvreader:
        Total.append(int(row[1]))
        date.append(row[0])
    print("Financial Analysis\n")
    print("-----------------------------------\n")
    print(f"Total Months: {(len(date))}")
    print(f"Total : ${sum(Total)}")
    for i in range(1,len(Total)):
        Total_change.append(Total[i] - Total[i-1])
        avg_Total_change = sum(Total_change)/len(Total_change)
        max_Total_change = max(Total_change)
        min_Total_change = min(Total_change)
        max_Total_change_date = str(date[Total_change.index(max(Total_change)) + 1])
        min_Total_change_date = str(date[Total_change.index(min(Total_change)) + 1])
    with open("Output.txt", "w") as text_file:
        print("Financial Analysis\n",file=text_file)
        print("----------------------------\n",file=text_file)
        print(f"Total Months: {(len(date))}",file=text_file)
        print(f"Total : ${sum(Total)}",file=text_file)
        print(f"Avereage Change: ${round(avg_Total_change ,2)}",file=text_file)
        print(f"Greatest Increase in Profits: {max_Total_change_date} (${(max_Total_change)})",file=text_file)
        print (f"Greatest Decrease in Profits: {min_Total_change_date} (${int(min_Total_change)})",file=text_file)
    print(f"Avereage Change: ${round(avg_Total_change ,2)}")
    print(f"Greatest Increase in Profits: {max_Total_change_date} (${(max_Total_change)})")
    print(f"Greatest Decrease in Profits: {min_Total_change_date} (${int(min_Total_change)})")
