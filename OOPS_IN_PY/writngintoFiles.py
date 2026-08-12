import json
import csv
txt_data = "modda gudu"

file_path = "output.txt"

with open(file_path,"w") as file:# methods are x,w,a,r, x is create a file only, if the file already exists then it will show an error 
#can also be declared as with open(file = file_path,mode = "w") for understanding
    file.write(txt_data)
    print(f"txt file {file_path} was created")
    
#these can also be made to put where ever we need by copything the pasth and using'/' there
# eg: filePath = "(path)/file_name"

try:
    with open(file_path,"x") as file:
        file.write(txt_data)
        file.write(txt_data)
except FileExistsError:
    print("File already exists")
print() 
file_path2 = "o3.txt"
try:
    with open(file_path2,"x"):
        print("File was created")#when the mode is append and the data should be written on the next line then 
        #file.write("\n"+txt_data)
        file.write(txt_data)
except:
    print("File was already existing")
    
#Memory Trick
#       w = Write → "Wipe and Write" (erases old content)
#       a = Append → "Add at the end"
#       x = eXclusive Create → "Create only if it doesn't already exist"

print()
print()
employees = ["hsfd","kdsf","aseka"]

try:
    with open(file_path2,"w") as file:
        for employee in employees:
            file.write(employee+"\n")
        print("Data was succesfullly entered")
except:
    print("FUHH NAHH")
    
employee = { #for json, it has key value pairs
    1:"BOB",
    2:"IUF",
    3:"FG"
}

file_path3="o2.json"

try:
    with open(file_path3,"w") as file:
        json.dump(employee,file,indent=4)# this will convert a dictionary into a json string
        print("Data (json)was succesfullly entered")
except:
    print("FUHH NAHH")
    
file_path4 = "o3.csv"
emp = [["name","Age","Job"],
       ["kjsdf",55,"asfhud"],
       ["ksadfh",69,"fsdhk"]]

print()
try:
    with open(file_path4,"w",newline="") as file:
        writer = csv.writer(file)# writer is used to write data into CSV file
        for row in emp:
            writer.writerow(row)
        print("Data (csv)was succesfullly entered")
except:
    print("FUHH NAHH")