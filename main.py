from utils import *

##########################
### JOB CONFIGURATIONS ###
##########################



########################
### BEGINNING OF ETL ###
########################

# Creating the folder to store the data
creating_folder(folder_name='./data')
# Creating the raw layer 
creating_folder(folder_name='./data/RAW')
# Creating the cleansed layer
creating_folder(folder_name='./data/CLEANSED')
# Creating the presentation layer
creating_folder(folder_name='./data/PRESENTATION')

# setting_credentials(config_path='./credentials.conf')

# extracting_file(url='https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset/data')

##################
### END OF ETL ###
##################