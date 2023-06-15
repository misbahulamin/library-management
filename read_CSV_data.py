import csv

with open('flight_shcudler_data.csv', 'r') as file:
    lines = csv.reader(file)
    for line in lines:
        print(line)