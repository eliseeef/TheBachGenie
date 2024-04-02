import csv
import json

def csv_to_json(csv_file, json_file):
    # Open the CSV file for reading
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        # Read the CSV file using a dictionary reader
        csvreader = csv.DictReader(csvfile)
        
        # Initialize an empty list to store rows
        data = []
        
        # Iterate over each row in the CSV file
        for row in csvreader:
            # Append the row as a dictionary to the data list
            data.append(row)
    
    # Write the data to a JSON file
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        # Serialize the data list to JSON and write it to the JSON file
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

# Example usage:
        
# - Missing: 3, 4, 6, 7, 8, 15, 16, 
seasonNumbers = [1, 2, 5, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]



csv_file_path = f'./all.csv'
json_file_path = f'./json/all.json'
csv_to_json(csv_file_path, json_file_path)
print(f'Conversion complete. JSON file saved at: {json_file_path}')

# for seasonNumber in seasonNumbers:
#     if (seasonNumber < 10):
#         csv_file_path = f'./season_0{seasonNumber}.csv'
#         json_file_path = f'./json/season_0{seasonNumber}.json'
#     else:
#         csv_file_path = f'./season_{seasonNumber}.csv'
#         json_file_path = f'./json/season_{seasonNumber}.json'
#     csv_to_json(csv_file_path, json_file_path)
#     print(f'Conversion complete. JSON file saved at: {json_file_path}')