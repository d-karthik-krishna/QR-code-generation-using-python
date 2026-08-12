import os

file_path = "file2.txt"
file_path2 = "OOPS_IN_PY/file1.txt"


if os.path.exists(file_path):
    print(f"FILE EXITS {file_path}")
else :
    print("It doesnt exist")
    
if os.path.exists(file_path2):
    if os.path.isfile(file_path2):
        print(f"FILE EXITS {file_path2} is a file")
else :
    print("It doesnt exist")
    