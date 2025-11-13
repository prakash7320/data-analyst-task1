import pandas as pd

df=pd.read_csv('C:/Users/ELCOT/Downloads/netflix_titles.csv')
print(df.info())
print(df.head())

#Handle Missing Values
df.isnull().sum()
print(df.isnull().sum())

#Remove Duplicates
df.drop_duplicates(inplace=True)
print(df.drop_duplicates(inplace=True))

#Standardize Text Columns
df['type'] = df['type'].str.strip().str.title()   
df['country'] = df['country'].str.title().str.strip()
df['rating'] = df['rating'].str.upper().fillna('NOT RATED')
print(df['type'].unique())
print(df['country'].head(10))
print(df['rating'].unique())

#Convert Dates
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

#Rename Columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

#Data Type Fixes
df['release_year'] = df['release_year'].astype(int)

df.to_csv('C:/Users/ELCOT/Downloads/clean_netflix_titles.csv', index=False)








