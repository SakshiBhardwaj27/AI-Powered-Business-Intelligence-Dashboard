import pandas as pd
import numpy as np

import ast

def parse_list_column(series):
    parsed = []

    for value in series:
        try:
            parsed.append(ast.literal_eval(value))
        except:
            parsed.append([])

    return parsed

def clean_data(df):
    """
    Cleans the Amazon Prime Titles dataset.
    """
    df = df.drop_duplicates(subset="id")
    # -------------------------
    # Fill Missing Values
    # -------------------------
    if "age_certification" in df.columns:
        df["age_certification"] = df["age_certification"].fillna("Unknown")

    if "seasons" in df.columns:
        df["seasons"] = df["seasons"].fillna(0)

    if "imdb_score" in df.columns:
        df["imdb_score"] = df["imdb_score"].fillna(df["imdb_score"].median())

    if "imdb_votes" in df.columns:
        df["imdb_votes"] = df["imdb_votes"].fillna(df["imdb_votes"].median())

    if "tmdb_score" in df.columns:
        df["tmdb_score"] = df["tmdb_score"].fillna(df["tmdb_score"].median())

    if "tmdb_popularity" in df.columns:
        df["tmdb_popularity"] = df["tmdb_popularity"].fillna(df["tmdb_popularity"].median())

    if "description" in df.columns:
        df["description"] = df["description"].fillna("Unknown")

    # -------------------------
    # Remove Duplicates
    # -------------------------
    dup_count = df.duplicated(subset="id").sum()
    df = df.drop_duplicates()

    # -------------------------
    # Runtime Outlier Check
    # -------------------------
    q1 = df["runtime"].quantile(0.25)
    q3 = df["runtime"].quantile(0.75)
    iqr = q3 - q1

    runtime_outliers = df[
        (df["runtime"] < q1 - 1.5 * iqr) |
        (df["runtime"] > q3 + 1.5 * iqr)
    ]

    # -------------------------
    # Display Cleaning Summary
    # -------------------------
    print(f"Duplicate title IDs removed: {dup_count}")
    print(f"Runtime outliers: {len(runtime_outliers)}")
    print(f"Min runtime: {df['runtime'].min()} min")
    print(f"Max runtime: {df['runtime'].max()} min")
    print(f"Release year: {df['release_year'].min()} - {df['release_year'].max()}")
    print(f"Titles before 1950: {(df['release_year'] < 1950).sum()}")
    print("Cleaning complete.")

    return df

def dataset_summary(df):

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }

    return summary

