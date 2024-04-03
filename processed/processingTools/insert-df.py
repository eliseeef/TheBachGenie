
import pandas as pd


def load_data_into_df():

    df = pd.read_csv('./generalized-data.csv')

    print(df.head())

    # print(df['job'].unique())

    print(df['hometown'].unique())
    print(df['job'].unique().size)


load_data_into_df()
