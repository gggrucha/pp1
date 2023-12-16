'''
21.	The products.csv file contains data about the products sold. Create the file in a text editor.
Product,Quantity,Price
milk,8,4.25
cheese,5,17.90
bread,21,6.15
juice,12,5.90
Then, write a program to convert data from CSV to JSON. The program reads product data from the 
CSV file and writes the data to a JSON file
'''
#chat

import csv
import json

# Function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    data = []

    # Read CSV file
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    # Write JSON file
    with open(json_file, 'w') as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))

# Input and output file paths
csv_file_path = 'products.csv'
json_file_path = 'products.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

print(f'Data converted from {csv_file_path} to {json_file_path}.')
