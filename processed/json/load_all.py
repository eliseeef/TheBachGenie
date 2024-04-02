









import json
import os

# Directory containing the JSON files
directory = './'

# Initialize an empty dictionary to hold the combined JSON data
combined_data = {}

# Iterate over each JSON file in the directory




for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            # Parse the JSON data from the file
            data = json.load(file)
            # Merge the data into the combined_data dictionary
            combined_data.update({filename: data})

# Convert the combined_data dictionary to a JSON string
combined_json = json.dumps(combined_data, indent=4)

# Write the combined JSON data to a file
with open('combined_data.json', 'w') as output_file:
    output_file.write(combined_json)

