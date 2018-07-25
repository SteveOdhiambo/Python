# CSV_module for parsing csv files
import csv

'''
csv.reader() - generates a reader object which is iterated to read rows of the file and print them
csv.writer() - generates a writer object suitable for writing
writerow() - to iterate the data over the rows
'''

with open('names.csv', 'r') as csv_file:
    # reader() uses a dialect that has preset parameters of what it expects the format of csv file to be
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        for line in csv_reader:
            csv_writer.writerow(line)
        # print(csv_writer)

with open('names.csv', 'r') as csv_file:
    csv_dictReader = csv.DictReader(csv_file)

    for line in csv_dictReader:
        print(line)