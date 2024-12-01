import os
import kagglehub
import configparser
import pprint
from pathlib import Path



def creating_folder(folder_name: str):
    '''
    DESCRIPTION: 
        It creates a folder that the data will be stored if that folder doesn't exist.
    
    PARAMETERS:
        - folder_name: name of the folder to create.
    '''
    path = f'./{folder_name}'

    try:
        os.mkdir(path)
    except FileExistsError as err:
        print(err)

def setting_credentials(config_path: str):
    '''
    DESCRIPTION:
        Define the credentials to connect to Kaggle's API

    PARAMETERS:
        - config_path: The path 
    '''
    config = configparser.ConfigParser()

    config.read(config_path)

    kaggle_username = config.get('kaggle', 'username')
    kaggle_key = config.get('kaggle', 'key')

    os.environ['KAGGLE_USERNAME'] = kaggle_username
    os.environ['KAGGLE_KEY'] = kaggle_key

    print(os.environ['KAGGLE_USERNAME'])
    print(os.environ['KAGGLE_KEY'])

    print('Kaggle credentials set successfully!')

def extracting_file(url: str):
    '''
    DESCRIPTION: 
        Extracts the .tsv files with the dataset from Kaggle's API
    
    PARAMETERS:
        - url: DNS hostname that the data is stored at.
    '''
    url_splitted = url.split('/')
    api_endpoint = f'{url_splitted[4]}/{url_splitted[5]}'
    print(api_endpoint)
    path = kagglehub.dataset_download(api_endpoint)
    print(f'Path to the dataset files: {path}')


path = kagglehub.dataset_download('ashirwadsangwan/imdb-dataset')
print(f'Path to the dataset files: {path}')

source_path = Path(path)
output_path = Path('E:\Documentos\IT\Repositório\IMDB\data\RAW')

for file in source_path.iterdir():
    if file.is_file():
        source_path.replace(output_path)
