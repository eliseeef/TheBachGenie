
import pandas as pd


def load_data_into_df():

    instagram_winners_df = pd.read_csv('./instagram_data/winners.csv')
    instagram_bachelors_df = pd.read_csv('./instagram_data/bachelors.csv')

    generalized_df = pd.read_csv('./pre_processing/generalized_data.csv')
    processed_df = pd.read_csv('./pre_processing/processed_data.csv')

    # Some people are missing from the generalized data, because we don't have all seasons
    print('Missing from generalized data:')
    for row in instagram_winners_df.iterrows():
        name = row[1]['name']
        name_in_generalized = generalized_df[generalized_df['name'] == name]
        if name_in_generalized.empty:
            print(f'{name}')

    print('\n\n\n')

    # Contestants with Discretization
    print(generalized_df.head(), end="\n\n\n")
    # Cleaned data without Discretization
    print(processed_df.head(), end="\n\n\n")
    # Instagram/Twitter data for winners and follower ups
    print(instagram_winners_df.head(), end="\n\n\n")
    # Instagram/Twitter data for bachelors
    print(instagram_bachelors_df.head(),end="\n\n\n")


load_data_into_df()
