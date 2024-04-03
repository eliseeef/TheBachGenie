import csv

# Mapping of states to regions
outcome_to_generalized = {
    "1": "earlyExit",
    "2": "earlyExit",
    "3": "earlyExit",
    "4": "earlyExit",
    "5": "midExit",
    "6": "midExit",
    "7": "midExit",
    "8": "midExit",
    "9": "lateExit",
    "10": "lateExit",
    "11": "lateExit",
    "12": "lateExit",
    "13": "lateExit",
    "14": "lateExit",
    "15": "lateExit",
    "16": "lateExit",
    "winner": "winner",
    "runnerUp": "runnerUp",
}

# Read the CSV file
with open('generalized-data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

# Update the hometowns to regions
for row in rows:
    outcome = row['outcome']
    region = outcome_to_generalized.get(outcome)
    if region:
        row['outcome'] = region
    else:
        print(f'Unknown outcome: {outcome}')
        row['outcome'] = None

# Write the updated data back to the CSV file
with open('updated_file.csv', 'w', newline='') as csvfile:
    fieldnames = ['season', 'name', 'age', 'hometown', 'job', 'outcome']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
