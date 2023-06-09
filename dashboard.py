import pandas as pd


# Get subject column value count
def get_value_counts(df):

    return dict(df["subject"].value_counts())


# get level count
def get_level_count(df):

    return dict(list(df.groupby(["level"])["num_subscribers"].count.items())[1:])


#