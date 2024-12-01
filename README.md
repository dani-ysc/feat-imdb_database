# IMDB dataset project
This project gets a IMDB dataset from Kaggle and apply transformations and store in a bucket in s3. The goal of the project is to generate a data product showing end to end the data engineering process of getting data from one place and stores it into the other.


STEPS:
1. Use the kagglehub to connect with the API to download the dataset programatically from the endpoint.
2. Creates raw buckets to store the data without any business logic, the cleansed bucket to store the dataset after transformations and the presentation that the output will go to the s3 bucket for the use of the data consumers.
3. Extract the .csv file from the zipfile.
4. Do Exploratory Data Analysis (EDA) to understand information from the dataset to develop the business logic that will generate a data product.
5. Use Pyspark to do the transformations and save the output files inside buckets.
6. Use Terraform to create the infrastructure of the jobs (using Airflow) and buckets in s3.
7. Store the data in s3.