## The libreary has been imported to read csv file
import csv
 
## A variable Budget_Dictionary created to store the change
Budget_Dictionary={}
## Variables for Total_Months, Total and Previous
Total_Months=0  
Total=0
Previous=0
flag=0

## Readding csv file
with open('Resources/budget_data.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    
    for lines in csvFile:
        ## Storing the header column names
        if flag == 0:
            header = lines
            
        ## Reading lines
        elif flag!=0:
            ## Summing up the total months
            Total_Months+=1
            ## getting current profit/loss value
            Current=int(lines[1])
            ## to find Changes, the first value is stored
            if flag==1: first_value=Current
            ## total is sum of profit/loss
            Total+=Current
            ## find out the change from previous month
            Change=Current - Previous
            ## storing in dict
            Budget_Dictionary[lines[0]]=Change
            Previous=Current
        flag+=1

## sorting the dictionary to get the greatest increase in profit and vice versa
Budget_sorted = sorted(Budget_Dictionary.items(),key = lambda kv: kv[1],reverse=True)
Average_Change = round((Current-  first_value)/Total_Months,2)
 
## storing analysis in text file. 
File_Analysis = open('Analysis/analysis_bank.txt', 'w')
print("\nFinancial Analysis")
File_Analysis.write("Financial Analysis\n")
print("-------------------------")

File_Analysis.write("-------------------------\n")
print("Total_Months: {0}".format(Total_Months))
File_Analysis.write("Total Months: {0}\n".format(Total_Months))
print("Total: ${0}".format(Total))
File_Analysis.write("Total: ${0}\n".format(Total))
print("Average Change: ${0}".format(Average_Change))
File_Analysis.write("Average Change: ${0}\n".format(Average_Change))
print("Greatest Inc in Profits: {0} (${1})".format(Budget_sorted[0][0],Budget_sorted[0][1]))
File_Analysis.write("Greatest Inc in Profits: {0} (${1})\n".format(Budget_sorted[0][0],Budget_sorted[0][1]))
print("Greatest Dec in Profits: {0} (${1})".format(Budget_sorted[-1][0],Budget_sorted[-1][1]))
File_Analysis.write("Greatest Dec in Profits: {0} (${1})\n".format(Budget_sorted[-1][0],Budget_sorted[-1][1]))
File_Analysis.close()
