import csv

# Open the input and output files
with open('../data/carbon_emissions_linechart.csv', mode='r') as infile, open('sorted_data.csv', mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Get the header
    header = next(reader)
    writer.writerow(header)

    # Define the order of states in 2001
    order_2001 = ['Johor', 'Kedah', 'Kelantan', 'Kuala Lumpur', 'Labuan', 'Melaka', 'Negeri Sembilan', 
                  'Pahang', 'Perak', 'Perlis', 'Pulau Pinang', 'Putrajaya', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu']

    # Create a dictionary to store data rows
    data_dict = {state: [] for state in order_2001}

    # Read and reorder data based on the 2001 order
    for row in reader:
        state = row[1]
        data_dict[state].append(row)

    # Write the sorted data to the output file
    for state in order_2001:
        for row in data_dict[state]:
            writer.writerow(row)
