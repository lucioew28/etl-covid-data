import chardet

with open('../MICRODADOS.csv', 'rb') as f:
    result = chardet.detect(f.read(1000))
    print(result['encoding'])