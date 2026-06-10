# old way
import os

file_path = "python_learning/small_topics/decorator.py"

if os.path.exists(file_path):
    print("file exists")
    if os.path.isfile(file_path):
        print("Is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else: 
    print("File doesnt exist")

# new way 
from pathlib import Path

file = Path("python_learning/small_topics/try_except_finally.py")

if file.exists:
    print("File exists")
    if file.is_file:
        print("Is a file")
    elif file.is_dir:
        print("Is a folder.")
else:
    print("File doesn't exist.")

# txt files
employees = ["spongebob","squidward","patrick","eugine"]
try:
    file_path1 = "C:/Users/User/OneDrive/Desktop/file1.txt"
    text = "I like pizza"
    with open(file_path1, 'a') as file:
        for employee in employees:
            print(file.write(employee + " "))
        print("Successful")
except FileExistsError:
    print("File already exists")
finally:
    file.close()

# json files 
import json

worker = {
    "name": "spongebob",
    "job": "cook",
    "species": "sponge",
    "age": 27,
}
file_path2 = "C:/Users/User/OneDrive/Desktop/file2.json"
try:
    with open(file_path2, mode="w") as file:
        json.dump(worker,file, indent=4)
        print(f"{file.name}:file was created")
except FileExistsError:
    print("File doesnt exist")
finally:
    file.close()

# csv files 

import csv

employee1 = [
    ["Name","Age","Ocuupation"],
    ["spongebob","30","cook"],
    ["patrick","37","unemployed"],
    ["sandy","27","scientist"]
    ]
file_path2 = r"C:\Users\User\OneDrive\Desktop\file3.csv"
with open(file_path2, "w",newline="") as file:
    try:
        writer = csv.writer(file)
        for row in employee1:
            writer.writerow(row)
        print(f"csv file {file.name} was created.")
    except FileExistsError:
        print("Fail already exist.")
    finally:
        file.close()