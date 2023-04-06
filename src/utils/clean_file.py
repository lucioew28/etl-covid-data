import pandas as pd

# Set the chunk size (number of rows to read at once)
chunksize = 100000

# Set the input and output file paths
input_file = '../MICRODADOS.csv'
output_file = 'OUTPUT_MICRODADOS.csv'

# Create a CSV reader object that reads the file in chunks
reader = pd.read_csv(input_file, chunksize=chunksize, encoding='ISO-8859-1', sep=';')

# Create a CSV writer object to write the output to a new file
writer = pd.DataFrame.to_csv(pd.DataFrame(columns=['Placeholder']), output_file, index=False)

# Loop through each chunk of data and process it
for chunk in reader:
    # Replace the NaN values with a default value (e.g. 0)
    chunk.fillna('', inplace=True)
    
    # Write the processed chunk to the output file
    with open(output_file, 'a') as f:
        chunk.to_csv(f, header=False, index=False)