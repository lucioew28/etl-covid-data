#check if wen can connect to this url

#download the file and show the pase on the terminal

# https://bi.s3.es.gov.br/covid19/MICRODADOS.csv

# pip intall tqdm : to show a progress bar of the file being downloaded

import requests
from tqdm import tqdm

def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()