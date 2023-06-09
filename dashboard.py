import pandas as pd


# Get subject column value count
def get_value_counts(df):

    return dict(df["subject"].value_counts())