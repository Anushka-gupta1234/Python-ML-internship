import csv 
def readfile(): 
    with open("data.csv","r") as file: 
        rec = csv.reader(file)  
    for i in rec: 
          print(i) 
 
readfile() 