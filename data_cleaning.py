import pandas as pd

def clean_data(df):

    print("----- DATA CLEANING STARTED -----")

    # remove duplicates
    df = df.drop_duplicates()

    # handle missing values
    df = df.fillna(method="ffill")

    print("Duplicates removed")
    print("Missing values handled")

    print("----- DATA CLEANING COMPLETED -----")

    return df