
import pandas as pd


def load_data_into_df():

    instagram_winners_df = pd.read_csv('./instagram_data/winners.csv')
    instagram_bachelors_df = pd.read_csv('./instagram_data/bachelors.csv')

    contestants_generalized = pd.read_csv('./personal_info/contestants_generalized.csv')
    contestants_processed = pd.read_csv('./personal_info/contestants_processed.csv')

    bachelors = pd.read_csv('./personal_info/bachelors.csv')

    # Some people are missing from the generalized data, because we don't have all seasons
    print('Missing from generalized data:')
    for row in instagram_winners_df.iterrows():
        name = row[1]['name']
        name_in_generalized = contestants_generalized[contestants_generalized['name'] == name]
        if name_in_generalized.empty:
            print(f'{name}')

    print('\n\n\n')

    # Contestants with Discretization
    print(contestants_generalized.head(), end="\n\n\n")
    # Cleaned data without Discretization
    print(contestants_processed.head(), end="\n\n\n")
    # Instagram/Twitter data for winners and follower ups
    print(instagram_winners_df.head(), end="\n\n\n")
    # Instagram/Twitter data for bachelors
    print(instagram_bachelors_df.head(),end="\n\n\n")
    # Bachelor data
    print(bachelors.head(),end="\n\n\n")


load_data_into_df()
