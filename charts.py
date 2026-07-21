import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

from utils import parse_list_column
# colorpalat with plotly
PRIME_BLUE = "#00A8E1"
PRIME_ORANGE = "#FF9900"
PRIME_DARK = "#0F1111"

COLORS = [
    "#00A8E1",
    "#FF9900",
    "#6DD5FA",
    "#FF6B6B",
    "#8E44AD",
    "#2ECC71",
    "#F4D03F"
]

# chat 1 
def plot_content_type(df):

    content = (
        df["type"]
        .value_counts()
        .reset_index()
    )

    content.columns = ["Type", "Count"]

    fig = px.bar(
        content,
        x="Type",
        y="Count",
        color="Type",
        color_discrete_sequence=[
            PRIME_BLUE,
            PRIME_ORANGE
        ],
        title="Movies vs TV Shows"
    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=PRIME_DARK,

        plot_bgcolor=PRIME_DARK,

        font=dict(size=16)
    )

    return fig

# Chart 2: Release Year Trend
def plot_release_year(df):

    release = (
        df["release_year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    release.columns = ["Year","Titles"]

    fig = px.line(

        release,

        x="Year",

        y="Titles",

        markers=True,

        color_discrete_sequence=[PRIME_BLUE],

        title="Titles Released Per Year"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=PRIME_DARK,

        plot_bgcolor=PRIME_DARK

    )

    return fig

# Chart 3: IMDb Score Distribution
def plot_imdb(df):

    fig = px.histogram(

        df,

        x="imdb_score",

        nbins=25,

        color_discrete_sequence=[PRIME_BLUE],

        title="IMDb Score Distribution"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=PRIME_DARK,

        plot_bgcolor=PRIME_DARK

    )

    return fig

# Chart 4: Runtime Distribution
def plot_runtime(df):

    fig = px.box(

        df,

        y="runtime",

        color_discrete_sequence=[PRIME_ORANGE],

        title="Runtime Distribution"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=PRIME_DARK,

        plot_bgcolor=PRIME_DARK

    )

    return fig

# Chart 5: Top 10 Genres
def plot_genres(df):

    genre = (

        df["genres"]

        .explode()

        .value_counts()

        .head(10)

        .reset_index()

    )

    genre.columns = [

        "Genre",

        "Count"

    ]

    fig = px.bar(

        genre,

        x="Count",

        y="Genre",

        orientation="h",

        color="Count",

        color_continuous_scale="Blues",

        title="Top 10 Genres"

    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor=PRIME_DARK,

        plot_bgcolor=PRIME_DARK

    )

    return fig

# age cirtification
def plot_age_certification(df):

    cert = (
        df["age_certification"]
        .value_counts()
        .head(12)
        .reset_index()
    )

    cert.columns = ["Age Certification", "Count"]

    fig = px.bar(
        cert,
        x="Age Certification",
        y="Count",
        color="Age Certification",
        color_discrete_sequence=COLORS,
        title="Content by Age Certification"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PRIME_DARK,
        plot_bgcolor=PRIME_DARK
    )

    fig.update_traces(textposition="outside", text=cert["Count"])

    return fig

# top geners
def plot_top_genres(df):

    temp = df.copy()

    temp["genres_list"] = parse_list_column(temp["genres"])

    genres = (
        temp
        .explode("genres_list")["genres_list"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    genres.columns = ["Genre", "Titles"]

    fig = px.bar(
        genres,
        x="Titles",
        y="Genre",
        orientation="h",
        color="Titles",
        color_continuous_scale="Blues",
        title="Top 15 Genres"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PRIME_DARK,
        plot_bgcolor=PRIME_DARK
    )

    return fig

# imdb vs tmdb 
def plot_imdb_vs_titles(df):

    yearly = (
        df[df["release_year"] >= 1980]
        .dropna(subset=["imdb_score"])
        .groupby("release_year")["imdb_score"]
        .agg(["mean", "count"])
    )

    yearly = yearly[yearly["count"] >= 5]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=yearly.index,
            y=yearly["mean"],
            mode="lines+markers",
            name="Average IMDb",
            line=dict(color=PRIME_BLUE, width=3)
        )
    )

    fig.add_trace(
        go.Bar(
            x=yearly.index,
            y=yearly["count"],
            name="Titles",
            opacity=0.4,
            marker_color=PRIME_ORANGE,
            yaxis="y2"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PRIME_DARK,
        plot_bgcolor=PRIME_DARK,
        title="Average IMDb Score & Title Count per Year",
        yaxis=dict(title="Average IMDb"),
        yaxis2=dict(
            title="Titles",
            overlaying="y",
            side="right"
        )
    )

    return fig

# corelation heatmap
def plot_heatmap(df):

    numeric = [
        "release_year",
        "runtime",
        "imdb_score",
        "imdb_votes",
        "tmdb_popularity",
        "tmdb_score"
    ]

    corr = df[numeric].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PRIME_DARK,
        plot_bgcolor=PRIME_DARK
    )

    return fig

# tmdb popularity 
def plot_tmdb_popularity(df):

    filtered = df[df["tmdb_popularity"] < 200]

    fig = px.scatter(
        filtered,
        x="imdb_score",
        y="tmdb_score",
        color="type",
        size="tmdb_popularity",
        hover_name="title",
        color_discrete_map={
            "MOVIE": PRIME_BLUE,
            "SHOW": PRIME_ORANGE
        },
        title="IMDb vs TMDb Scores"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PRIME_DARK,
        plot_bgcolor=PRIME_DARK
    )

    return fig

# countries 
def plot_countries(df):

    temp = df.copy()

    temp["countries_list"] = parse_list_column(
        temp["production_countries"]
    )

    countries = (
        temp
        .explode("countries_list")["countries_list"]
        .value_counts()
        .head(15)
        .reset_index()
    )

    countries.columns = [
        "Country",
        "Titles"
    ]

    fig = px.bar(
        countries,
        x="Titles",
        y="Country",
        orientation="h",
        color="Titles",
        color_continuous_scale="Plasma",
        title="Top 15 Production Countries"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PRIME_DARK,
        plot_bgcolor=PRIME_DARK
    )

    return fig

