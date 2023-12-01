import os 
import statistics
import csv 
monthcount = 0
totalvolume = 0
monthchange = []
avgchange = 0 
monthbymonth = []
months = []
data = {}
maxvalue = 0
minvalue = 0
bank_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(bank_csv,encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     
    Header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        monthcount = monthcount + 1
        totalvolume = totalvolume + int(row[1])
        monthchange.append(int(row[1]))
        
        
print("Total Months:", str(monthcount) )
print("Total Volume:", str(totalvolume))  

    #print(monthchange)
    
#for x in range(len(monthchange)-1):
    #avgchange = (monthchange[x+1]-monthchange[x])
    #monthbymonth.append(avgchange)
   # maxvalue = max(monthbymonth)
    #minvalue = min(monthbymonth)
print("Average Month: $", round(statistics.mean(monthbymonth),2))

print(max(monthbymonth))
print(data)







