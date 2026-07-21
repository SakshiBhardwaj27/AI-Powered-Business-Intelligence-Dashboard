import streamlit as st
import ast

# ===========================
# Sidebar Filters
# ===========================
def apply_filters(df):
    st.sidebar.header("🎯 Filters")

    content_type = st.sidebar.multiselect(
        "Content Type",
        options=sorted(df["type"].dropna().unique()),
        default=sorted(df["type"].dropna().unique())
    )   
    year_range = st.sidebar.slider(
        "Release Year",
        int(df["release_year"].min()),
        int(df["release_year"].max()),
        (
            int(df["release_year"].min()),
            int(df["release_year"].max())
        )
    )   
    rating_range = st.sidebar.slider(
        "IMDb Rating",
        0.0,
        10.0,
        (
            float(df["imdb_score"].min()),
            float(df["imdb_score"].max())
        )
    )
    age_filter = st.sidebar.multiselect(
        "Age Certification",
        options=sorted(df["age_certification"].dropna().unique()),
        default=sorted(df["age_certification"].dropna().unique())
    )

    country_set = set()

    for value in df["production_countries"].dropna():

        try:
            countries = ast.literal_eval(value)

            country_set.update(countries)

        except:
            pass

    country_filter = st.sidebar.multiselect(

        "Country",

        sorted(list(country_set))
    )

    # apply filters
    filtered_df = df.copy()
    filtered_df = filtered_df[
        filtered_df["type"].isin(content_type)
    ]
    filtered_df = filtered_df[
        (filtered_df["release_year"] >= year_range[0]) &
        (filtered_df["release_year"] <= year_range[1])
    ]
    filtered_df = filtered_df[
        (filtered_df["imdb_score"] >= rating_range[0]) &
        (filtered_df["imdb_score"] <= rating_range[1])
    ]
    filtered_df = filtered_df[
        filtered_df["age_certification"].isin(age_filter)
    ]
    if country_filter:

        filtered_df = filtered_df[

            filtered_df["production_countries"].apply(

                lambda x:

                any(

                    c in str(x)

                    for c in country_filter

                )

            )

        ]
    return filtered_df