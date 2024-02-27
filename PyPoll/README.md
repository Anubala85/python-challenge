**PART A:

In in this section have declared variables for total  number of votes and winner votes and also created a dictonary for the candidate info.

**PART B

In this section I have given the path for the csv file that was provided. This is the data  with which we iterate to find our results.
we have written the code to open the csv file and also are using csv reader to tell how to read the data from the given file.
 
**PART C

In this section I am using a FOR loop to read the record in csv reader and by mentioning the index from where to pull the Candidate Name.

**PART D

1.In this section I am using a If statement where I check for candidate Name not equal to "candidate" because we want the program to start iterating through the next row because current row is the header.

2.Here I am using a If/Else statement to check for candidate name if its not in candidate info then am asking it to add it to the candidate info dictionary and count the number of votes. if there is a new candidate name we ask to add it to the candidate ifo and start counting the number of votes from 1. Likewise we iterate the given list and calculate total votes cast across each candidate.

#PART E
1.In this section I have printed my results uisng print function.Used a "f" function to "print election results" and "total votes".
2.Have used a For loop here to find out percenatage votes for each poll candidate and priniting the percentage votes along side the candidate name.
3.Last have used a If statement that calculates the candiate with maximum number of votes.
4.using print name declaring the winner.
5.Finally have written code to rint the the results in a text file.

**REFERENCES

1.used stackoverflow to understand how to write code to exxport it as text file.