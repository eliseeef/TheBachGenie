
import pandas as pd


def load_data_into_df():

    winners_df = pd.read_csv('./winners.csv')
    bachelors_df = pd.read_csv('./bachelors.csv')


    generalized_df = pd.read_csv('../pre_processing/generalized_data.csv')

    print("Some people are missing from the generalized data, because we don't have all seasons:")
    for row in winners_df.iterrows():
        name = row[1]['name']
        name_in_generalized = generalized_df[generalized_df['name'] == name]
        if name_in_generalized.empty:
            print(f'{name}')

        

        

    print(winners_df.head())
    print(bachelors_df.head())
    print(generalized_df.head())



load_data_into_df()
