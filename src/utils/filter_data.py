import pandas as pd

def filter_data(pathtodata, datafiltered):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(pathtodata, nrows=1000, sep=';', encoding='ISO-8859-1')

    # Replace all NaN values with an -
    filtered_df = df.fillna('')

    # Replace "Não" with False and "Sim" with True
    filtered_df = filtered_df.replace({'Não': False, 'Sim': True})

    # Write the filtered data to a new CSV file
    filtered_df.to_csv(datafiltered, index=False)

    # Print a message to confirm the operation is complete
    print('\U0001F642 Filtered data has been written to ', datafiltered)