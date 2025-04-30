import csv

#a function name extract_second_field that extract the second field from a csv file
def extract_second_field(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        second_field = []
        for row in reader:
            if len(row) >= 2:
                second_field.append(row[1])
        return second_field
    
print(extract_second_field('data.csv'))