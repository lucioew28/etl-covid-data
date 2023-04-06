from src.utils.download_file import download_file

url = 'https://bi.s3.es.gov.br/covid19/MICRODADOS.csv'
filename = 'MICRODADOS.csv'

# download the MICRODADOS.csv file to the root directory
download_file(url, filename)

# clean the data before inserting it into the staging area
