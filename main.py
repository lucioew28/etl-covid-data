from src.utils.download_file import download_file
from src.utils.filter_data import filter_data
from src.database.staging_area import create_table

url = 'https://bi.s3.es.gov.br/covid19/MICRODADOS.csv'
filename = './files/MICRODADOS.csv'

# download the MICRODADOS.csv file into the files directory
# download_file(url, filename)


# clean the data before inserting it into the staging area
outputPath = './files/MICRODADOS_TREATED.csv'
filter_data(filename, outputPath)

#create the staging area
create_table()

# inserting the data to the database
# insert_into_db()

