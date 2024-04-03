import csv
import json



def combine_csv_files(csv_files, combined_csv_file):
    # Initialize an empty list to store rows
    data = []

    # Iterate over each CSV file
    for csv_file in csv_files:
        # Open the CSV file for reading
        with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            # Read the CSV file using a dictionary reader
            csvreader = csv.DictReader(csvfile)

            # Iterate over each row in the CSV file
            for row in csvreader:
                # Append the row as a dictionary to the data list
                data.append(row)
                # Add a column to indicate the source CSV file
                row['source'] = csv_file

    # Write the data to a combined CSV file
    with open(combined_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Get the fieldnames from the first row of the data
        fieldnames = data[0].keys()

        # Create a dictionary writer
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the fieldnames to the CSV file
        csvwriter.writeheader()

        # Iterate over each row in the data
        for row in data:
            # Write the row to the CSV file
            csvwriter.writerow(row)


csvFiles = [
    './season_01.csv',
    './season_02.csv',
    './season_05.csv',
    './season_09.csv',
    './season_10.csv',
    './season_11.csv',
    './season_12.csv',
    './season_13.csv',
    './season_14.csv',
    './season_17.csv',
    './season_18.csv',
    './season_19.csv',
    './season_20.csv',
    './season_21.csv',
    './season_22.csv',
    './season_23.csv',
    './season_24.csv',
    './season_25.csv',
    './season_26.csv',
    './season_27.csv',
    './season_28.csv'
]


combined_csv_file = './all-seasons.csv'
combine_csv_files(csvFiles, combined_csv_file)
print(f'Combination complete. CSV file saved at: {combined_csv_file}')
