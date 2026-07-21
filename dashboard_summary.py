import pandas as pd
import ast

def create_dashboard_summary(df):

    summary = {}

    summary["Total Titles"] = len(df)

    summary["Movies"] = (df["type"] == "MOVIE").sum()

    summary["Shows"] = (df["type"] == "SHOW").sum()

    summary["Average IMDb"] = round(df["imdb_score"].mean(), 2)

    summary["Average Runtime"] = round(df["runtime"].mean(), 2)

    summary["Release Year Range"] = (
        f"{df['release_year'].min()} - {df['release_year'].max()}"
    )

    # Top Genre
    genres = []

    for value in df["genres"]:

        try:
            genres.extend(ast.literal_eval(value))
        except:
            continue

    genre_counts = pd.Series(genres).value_counts()

    summary["Top Genre"] = genre_counts.index[0] if not genre_counts.empty else "N/A"

    return summary