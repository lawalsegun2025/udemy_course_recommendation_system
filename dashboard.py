import pandas as pd


# Get subject column value count
def get_value_counts(df):

    return dict(df["subject"].value_counts())


# get level count
def get_level_count(df):

    return dict(list(df.groupby(["level"])["num_subscribers"].count().items())[1:])


# get subjects per level
def get_subjects_per_level(df):

    ans = list(dict(df.groupby(['subject'])['level'].value_counts()).keys())
    all_labels = [ans[i][0]+"_"+ans[i][1] for i in range(len(ans))]
    all_values =list(dict(df.groupby(["subject"])["level"].value_counts()).values())
    complete_dict = dict(zip(all_labels, all_values))

    return complete_dict