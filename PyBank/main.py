import os
import csv

#PART A

reportedmonth = []
profitloss = []
total_profitloss = 0
rowCount = -1
nRecords = 0
greatestIncrease = 0
greatestDecrease = 0
totalprofitlossChange = 0

#PART B

budget_csv = os.path.join("Resources","budget_data.csv")

with open (budget_csv) as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")

#PART C
    
    for row in csvreader:
        rowCount = rowCount + 1

        if rowCount > 0:
            reportedmonth.append (row[0])
            profitloss.append (row[1])
            total_profitloss = total_profitloss + int (row[1])
            
            if rowCount > 1:
                
                profitlossChange = int (profitloss[rowCount-1]) - int (profitloss[rowCount - 2])
                totalprofitlossChange = totalprofitlossChange + profitlossChange
                
                if profitlossChange > greatestIncrease:
                    greatestIncrease = profitlossChange
                    greatestIncrease_month = row[0]
                if profitlossChange < greatestDecrease:
                    greatestDecrease = profitlossChange
                    greatestDecrease_month = row[0]

#PART D 
                    
nRecords = len (reportedmonth)
averageChange_profitloss = round (totalprofitlossChange / (nRecords - 1), 2)

resultsFile = open ("Results.txt", "w")

print (f"Financial Analysis")
resultsFile.write ("Financial Analysis \n")

print (f"--------------------")
resultsFile.write ("--------------------\n")

print (f"Total Months: {nRecords}")
resultsFile.write ("Total Months: " + str (nRecords) + "\n")

print (f"Total: ${total_profitloss}")
resultsFile.write ("Total: $" + str (total_profitloss) + "\n")

print (f"Average Change: ${averageChange_profitloss}")
resultsFile.write ("Average Change: $" + str (averageChange_profitloss) + "\n")

print (f"Greatest Increase in Profits: {greatestIncrease_month} (${greatestIncrease})")
resultsFile.write ("Greatest Increase in Profits: " + greatestIncrease_month + " ($" + str (greatestIncrease) + ")\n")

print (f"Greatest Decrease in Profits: {greatestDecrease_month} (${greatestDecrease})")
resultsFile.write ("Greatest Decrease in Profits: " + greatestDecrease_month + " ($" + str (greatestDecrease) + ")\n")

resultsFile.close ()