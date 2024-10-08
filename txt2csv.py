import csv

with open('cleaned-ocr-output.txt', 'r') as file:
    data = file.read()

# Processing each line of the input data
lines = data.split('\n')

# List to store rows for CSV
rows = []

# Loop through the lines to extract street names and prices
for line in lines:
    split_point = 0
    for i in range(split_point, len(line)):
        if not line[i].isnumeric():
            split_point = i
            break

    dataLine = line[split_point:].split()  # Extract street name

    rows.append([line[0:split_point], dataLine[0].strip(), dataLine[-1].strip()])

# Writing the extracted data to a CSV file
with open('streets_prices.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header row
    csvwriter.writerow(['Index', 'Street Name', 'Price Range'])
    
    # Write the data rows
    csvwriter.writerows(rows)

print("Data has been successfully written to 'streets_prices.csv'.")