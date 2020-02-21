import csv
import pandas as pd
# when we are getting data from url
import requests


def get_file(filename,column_names):
    data_df = pd.read_csv('static/'+filename)
    data_interest = data_df[column_names]
    data_interest.to_json('data.json')

