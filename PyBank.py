import os
import csv
Total_months = 0
Total = 0
max_profit = 0
min_profit = 0
monthly_diff = 0
Total_monthly_diff = 0
Avg_monthly_diff = 0
temp = None
i = 0
max_profit_date = None
min_profit_date = None

budget_dataCSV = os.path.join('budget_data.csv')
with open(budget_dataCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in csvreader:
        p = int(row[1])
        #monthly_diff = i - int(row[1])
        #max_profit = max(p,monthly_diff)
        #p = int(row[1])
        #max_profit = max(p,max_profit)
        #min_profit = min(p,min_profit)
        #if(max_profit) == int(row[1]):max_profit_date = row[0]
        #if(min_profit) == int(row[1]):min_profit_date = row[0]
        Total_months = Total_months + 1
        if temp is not None:
            monthly_diff = temp - int(row[1])
            max_profit = max(monthly_diff,temp)
            Total_monthly_diff  = Total_monthly_diff - monthly_diff

        Total = Total + int(row[1])
        temp = int(row[1])
    Avg_mon_diff = Total_monthly_diff / (Total_months - 1)
    with open("Output.txt", "w") as text_file:
        print("Financial Analysis\n",file=text_file)
        print("----------------------------\n",file=text_file)
        print(f"Total Months: {Total_months}",file=text_file)
        print(f"Total : ${Total}",file=text_file)
        print(f"Average  Change: ${Avg_mon_diff}",file=text_file)
        print(f"The greatest increase in profits: {max_profit_date} (${max_profit}) ",file=text_file)
        print (f"The greatest decrease in profits: {min_profit_date} (${min_profit}) ",file=text_file)

    print("Financial Analysis\n")
    print("----------------------------\n")
    print(f"Total Months: {Total_months}")
    print(f"Total : ${Total}")
    print(f"Average  Change: ${Avg_mon_diff}")
    print(f"The greatest increase in profits: {max_profit_date} (${max_profit}) ")
    print (f"The greatest decrease in profits: {min_profit_date} (${min_profit}) ")
