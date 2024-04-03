
import pandas as pd


def load_data_into_df():

    df = pd.read_csv('./all-seasons.csv')

    print(df.head())

    # print(df['job'].unique())
    print('[')
    for job in df['hometown'].unique():
        print(f'"{job}", ')
    print(']')


load_data_into_df()
