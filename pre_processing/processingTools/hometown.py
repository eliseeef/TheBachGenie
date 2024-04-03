import csv

# Mapping of states to regions
state_to_region = {
    "Alaska": "West",
    "Arizona": "West",
    "California": "West",
    "Colorado": "West",
    "Hawaii": "West",
    "Idaho": "West",
    "Montana": "West",
    "Nevada": "West",
    "New Mexico": "West",
    "Oregon": "West",
    "Utah": "West",
    "Washington": "West",
    "Wyoming": "West",
    "Illinois": "Midwest",
    "Indiana": "Midwest",
    "Iowa": "Midwest",
    "Kansas": "Midwest",
    "Michigan": "Midwest",
    "Minnesota": "Midwest",
    "Missouri": "Midwest",
    "Nebraska": "Midwest",
    "North Dakota": "Midwest",
    "Ohio": "Midwest",
    "South Dakota": "Midwest",
    "Wisconsin": "Midwest",
    "Connecticut": "Northeast",
    "Maine": "Northeast",
    "Massachusetts": "Northeast",
    "New Hampshire": "Northeast",
    "Rhode Island": "Northeast",
    "Vermont": "Northeast",
    "Delaware": "South",
    "Florida": "South",
    "Georgia": "South",
    "Maryland": "South",
    "North Carolina": "South",
    "South Carolina": "South",
    "Virginia": "South",
    "West Virginia": "South",
    "Alabama": "South",
    "Kentucky": "South",
    "Mississippi": "South",
    "Tennessee": "South",
    "Arkansas": "South",
    "Louisiana": "South",
    "Oklahoma": "South",
    "Texas": "South",
    "New Jersey": "Northeast",
    "New York": "Northeast",
    "Pennsylvania": "Northeast",
}

# Read the CSV file
with open('generalized-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Update the hometowns to regions
for row in rows:
    hometown = row['hometown']
    state = hometown.split(', ')[-1]
    region = state_to_region.get(state)
    if region:
        row['hometown'] = region
    else:
        row['hometown'] = 'Foreign'

# Write the updated data back to the CSV file
with open('updated_file.csv', 'w', newline='') as csvfile:
    fieldnames = ['season', 'name', 'age', 'hometown', 'job', 'outcome']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
