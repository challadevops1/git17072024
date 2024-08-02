# L4 - Create Python Console Application to readthe contents of .json file and print in the VS Code python console output

# Python program to read
# json file

import json

# Opening JSON file
f = open('C:/Users/C Babu/venv/GitDemol4&l5/git17072024/myfile.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['employees']:
    print(i)

# Closing file
f.close()