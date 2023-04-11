import chardet

# path to the file
file_path = '/home/lucio/Projects/faesa/bi/etl_project/MICRODADOS.csv'

# open the file in binary mode
with open(file_path, 'rb') as f:
    # read the first 1000 bytes of the file
    raw_data = f.read(1000)
    # detect the encoding of the raw data
    result = chardet.detect(raw_data)
    # print the detected encoding
    print(result['encoding'])
