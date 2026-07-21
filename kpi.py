import streamlit as st
import pandas as pd

def show_kpis(df):

    st.subheader("📊 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Titles",
            len(df)
        )

    with col2:
        st.metric(
            "Movies",
            (df["type"] == "MOVIE").sum()
        )

    with col3:
        st.metric(
            "TV Shows",
            (df["type"] == "SHOW").sum()
        )

    with col4:
        st.metric(
            "Average IMDb",
            round(df["imdb_score"].mean(), 2)
        )

def dataset_summary(df):

    st.subheader("📁 Dataset Summary")

    st.write(f"Rows : {df.shape[0]}")
    st.write(f"Columns : {df.shape[1]}")

    st.write("Columns")

    st.write(df.columns.tolist())

# Content Insights
def content_insights(df):

    st.subheader("🎬 Content Insights")

    most_common_type = df["type"].mode()[0]

    top_certification = (
        df["age_certification"]
        .value_counts()
        .idxmax()
    )

    latest_year = int(df["release_year"].max())

    oldest_year = int(df["release_year"].min())

    st.success(
        f"""
• Most content consists of **{most_common_type}**.

• Most common age certification is **{top_certification}**.

• Dataset spans from **{oldest_year}** to **{latest_year}**.
"""
    )

# Rating Insights
def rating_insights(df):

    st.subheader("⭐ Rating Insights")

    highest = df.loc[
        df["imdb_score"].idxmax()
    ]

    lowest = df.loc[
        df["imdb_score"].idxmin()
    ]

    st.info(
        f"""
Highest Rated

{highest['title']}

IMDb : {highest['imdb_score']}
"""
    )

    st.warning(
        f"""
Lowest Rated

{lowest['title']}

IMDb : {lowest['imdb_score']}
"""
    )

# Runtime Insights
def runtime_insights(df):

    st.subheader("⏱ Runtime")

    st.write(
        f"Average Runtime : {round(df['runtime'].mean(),1)} minutes"
    )

    st.write(
        f"Longest Runtime : {df['runtime'].max()} minutes"
    )

    st.write(
        f"Shortest Runtime : {df['runtime'].min()} minutes"
    )

# Top Genres
import ast
def genre_insights(df):

    genres = []

    for value in df["genres"].dropna():

        try:
            genres.extend(ast.literal_eval(value))

        except:
            pass

    top = pd.Series(genres).value_counts().head(5)

    st.subheader("🎭 Top Genres")

    st.table(top)

# top countries
def country_insights(df):

    countries = []

    for value in df["production_countries"].dropna():

        try:
            countries.extend(ast.literal_eval(value))

        except:
            pass

    top = pd.Series(countries).value_counts().head(5)

    st.subheader("🌍 Top Countries")

    st.table(top)

# Data Quality Report
def quality_report(df):

    st.subheader("🛠 Data Quality")

    quality = pd.DataFrame({

        "Missing Values": df.isnull().sum(),

        "Data Type": df.dtypes.astype(str)

    })

    st.dataframe(quality)