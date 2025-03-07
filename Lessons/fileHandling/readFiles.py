# .txt
# file_path = "input.txt"
#
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")

# .json
# import json
# file_path = "input.json"
#
# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["name"])
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that file")

# .csv

import csv
file_path = "input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")