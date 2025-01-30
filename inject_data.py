import pandas as pd
from sqlalchemy import create_engine
import argparse
import os 

def main(params):
    # Connection made to postgres database
    engine = create_engine(f'postgresql://{params.username}:{params.password}@{params.host}:{params.port}/{params.db}')

    # List of filenames that needs to be inserted in postgres
    file_name = ['average_engagement_time', 'country', 'new_users', 'user_count']

    # Iterating through all the files and inserting each in there individual table
    for i in range(len(file_name)): 
        df = pd.read_csv(f'{file_name[i]}.csv')
        df.head(0).to_sql(name=file_name[i], con=engine, if_exists='replace')
        df.to_sql(name=file_name[i], con=engine, if_exists='append')
        print(f'Inserted {file_name[i]} !!')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("password")
    parser.add_argument("host")
    parser.add_argument("port")
    parser.add_argument("db")
    args = parser.parse_args()
    main(args)