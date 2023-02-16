## The libreary has been imported to read csv file
import csv
 
## A variable Dictionary has been created to store the Election votes.
Election_Dictionary={}
## number of votes.
Votes=0
flag=0

##Reading csv file
with open('Resources/election_data.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    
    for lines in csvFile:
        ## storing header columns
        if flag == 0:
            header = lines
            
        elif flag!=0:
            ## total votes 
            Votes+=1
            ## checking of a candidate who is not in dictionary, then add to dictionary
            ## if in dictionary then increment vote
            if lines[2] not in Election_Dictionary:
                Election_Dictionary[lines[2]]=1
                
            else:
                Election_Dictionary[lines[2]]+=1
        flag+=1

## storing analysis result to be in text file (variable) called File_Election_Analysis     
File_Election_Analysis = open('Analysis/Analysis_Election.txt', 'w')
    
print("\nElection Results")
File_Election_Analysis.write("Election Results\n")
print("---------------------\n---------------------\n                        ")


File_Election_Analysis.write("-------------------------\n")
print("Total Votes: {0}".format(Votes))
File_Election_Analysis.write("Total Votes: {0}\n".format(Votes))
print("-------------------------")
File_Election_Analysis.write("-------------------------\n")

for name in Election_Dictionary:
    Percentage = round((Election_Dictionary[name]/Votes)*100,3)
    print("{0}: {1}% ({2})".format(name, Percentage, Election_Dictionary[name]))
    File_Election_Analysis.write("{0}: {1}% ({2})\n".format(name, Percentage, Election_Dictionary[name]))
    
print("-------------------------")
File_Election_Analysis.write("-------------------------\n")
Election_Sorted = sorted(Election_Dictionary.items(),key = lambda kv: kv[1],reverse=True)
print("Winner: {0}".format(Election_Sorted[0][0]))
File_Election_Analysis.write("Winner: {0}\n".format(Election_Sorted[0][0]))
print("-------------------------")
File_Election_Analysis.write("-------------------------\n")
File_Election_Analysis.close()
