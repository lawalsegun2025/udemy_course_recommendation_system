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


# Get year wise profit
def year_wise_profit(df):

    # Get profit
    df["profit"] = df["price"] * df["num_subscribers"]

    # dropping of that index which has '3 hours' as time
    df = df.drop(df.index[2066])

    # Get published_date column from published_timestamp column
    df['published_date'] = df['published_timestamp'].apply(lambda x:x.split('T')[0])

    # converting the published date to pandas datetime object
    df['published_date'] = pd.to_datetime(df['published_date'],format="%Y-%m-%d")

    # Get year
    df['Year'] = df['published_date'].dt.year

    # Get month number
    df['Month'] = df['published_date'].dt.month

    # Get day
    df['Day'] = df['published_date'].dt.day

    # get month name
    df['Month_name'] = df['published_date'].dt.month_name()

    # Get profit map by year
    profit_map = dict(df.groupby(['Year'])['profit'].sum())

    # get yearly number of subscribers
    subscribers_map = dict(df.groupby(['Year'])['num_subscribers'].sum())

    # Get profit map by month
    profit_month_wise = dict(df.groupby(['Month_name'])['profit'].sum())

    # Number of subscribers by month
    month_wise_sub = dict(df.groupby(['Month_name'])['num_subscribers'].sum())

    return profit_map, subscribers_map, profit_month_wise, month_wise_sub