import pandas as pd
import ast

def get_dataset_summary(df):

    summary = {}

    summary["Rows"] = len(df)

    summary["Columns"] = len(df.columns)

    summary["Movies"] = len(df[df["type"]=="MOVIE"])

    summary["Shows"] = len(df[df["type"]=="SHOW"])

    summary["Average IMDb"] = round(df["imdb_score"].mean(),2)

    summary["Average Runtime"] = round(df["runtime"].mean(),2)

    summary["Newest Year"] = int(df["release_year"].max())

    summary["Oldest Year"] = int(df["release_year"].min())

    return summary

# geners summry
def top_genres(df):

    genres=[]

    for value in df["genres"]:

        try:
            genres.extend(ast.literal_eval(value))
        except:
            continue

    return pd.Series(genres).value_counts().head(10)

# country 
def top_countries(df):

    countries=[]

    for value in df["production_countries"]:

        try:
            countries.extend(ast.literal_eval(value))
        except:
            continue

    return pd.Series(countries).value_counts().head(10)