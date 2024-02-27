import os
import csv

#PART A

candidateInfo = {}
totalVotes = 0 
winnerVotes = -1

#PART B

election_csv = os.path.join("Resources","election_data.csv")

with open (election_csv) as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ",")

#PART C
    
    for record in csvreader:
        candidateName = record[2]

#PART D
        
        if candidateName != "Candidate": # file starts with a header hence skip first record
            totalVotes = totalVotes + 1 
        
            if candidateName in candidateInfo:
                candidateInfo[candidateName] = candidateInfo[candidateName] + 1
            else:
                candidateInfo[candidateName] = 1
#PART E
    
    resultsFile = open ("Results.txt", "w")

    print (f"Election Results")
    resultsFile.write ("Election Results \n")

    print (f"---------------------")
    resultsFile.write ("--------------------- \n")

    print (f"Total Votes: {totalVotes}")
    resultsFile.write ("Total Votes: " + str (totalVotes) + "\n")

    print (f"---------------------")
    resultsFile.write ("--------------------- \n")
    
    for key in candidateInfo:

        votesPercent = round (candidateInfo[key] * 100 / totalVotes, 3)
        
        print (f"{key} : {votesPercent}% ({candidateInfo[key]})")
        resultsFile.write (str(key) + " : " + str(votesPercent) + "%" + " (" + str (candidateInfo[key]) +") \n")
        
        if winnerVotes <= candidateInfo[key]:
            winnerVotes = candidateInfo[key]
            winnerName = key

    print (f"---------------------")
    resultsFile.write ("---------------------\n")

    print (f"Winner: {winnerName}")
    resultsFile.write ("Winner:" + winnerName + "\n")

    resultsFile.close()









