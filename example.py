import csv

#a function name extract_second_field that extracts only the second field from csv and put it in a list
def extract_second_field(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        second_field = [row[1] for row in reader]
    return second_field


print(extract_second_field('data.csv'))