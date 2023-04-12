from src.utils.download_file import download_file
from src.utils.filter_data import filter_data
from src.database.staging_area import create_table
from src.database.insert_data import import_csv_to_postgresql
from src.database.create_star_schema import create_fact_table
from src.database.populate_star_schema import populate_star_schema

url = 'https://bi.s3.es.gov.br/covid19/MICRODADOS.csv'
filename = './files/MICRODADOS.csv'

# download the MICRODADOS.csv file into the files directory
download_file(url, filename)


# clean the data before inserting it into the staging area
outputPath = './files/MICRODADOS_TREATED.csv'
filter_data(filename, outputPath)

#create the staging area
create_table()

# inserting the data to the database
import_csv_to_postgresql('./files/MICRODADOS_TREATED.csv', 'staging')

# create the fact table and its dimentios
create_fact_table()

# populate star schema
populate_star_schema()