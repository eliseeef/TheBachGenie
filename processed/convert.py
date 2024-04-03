import csv
import json


def combine_csv_files(csv_files, combined_csv_file):
    data = []

    for csv_file in csv_files:
        with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                data.append(row)
                row['source'] = csv_file

    with open(combined_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()

        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csvwriter.writeheader()

        for row in data:
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


def load_data_into_df():
    import pandas as pd

    df = pd.read_csv('./all-seasons.csv')

    print(df.head())
    return df
