import streamlit as st

from charts import *
from kpi import show_kpis

def show_dashboard(df):
    show_kpis(df)
    st.title("Amazon Prime Dashboard")
    
    tab1, tab2, tab3 = st.tabs([
        "Overview",
        "Ratings",
        "Content"
    ])

    with tab1:

        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(
                plot_content_type(df),
                use_container_width=True,
                key="content_type_chart"
            )

        with col2:
            st.plotly_chart(
                plot_release_year(df),
                use_container_width=True,
                 key="release_year_chart"
            )
        col3,col4 = st.columns(2)

    with col3:

        st.plotly_chart(
            plot_age_certification(df),
            use_container_width=True,
            key="age"
        )

    with col4:

        st.plotly_chart(
            plot_runtime(df),
            use_container_width=True,
            key="runtime"
        )

    with tab2:

        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(
                plot_imdb(df),
                use_container_width=True,
                key="imdb_chart"
            )

        with col2:
            st.plotly_chart(
                plot_heatmap(df),
                use_container_width=True,
                key="heatmap"
            )
        col3,col4 = st.columns(2)

        with col3:
            st.plotly_chart(
                plot_imdb_vs_titles(df),
                use_container_width=True,
                key="imdbyear"
            )
        with col4:
            st.plotly_chart(
                plot_tmdb_popularity(df),
                use_container_width=True,
                key="tmdb"
            )

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(
                plot_top_genres(df),
                use_container_width=True,
                key = "Top geners"
        )
        with col2:
            st.plotly_chart(
                plot_countries(df),
                use_container_width=True,
                key="countries"
        )

with st.expander("Dataset Statistics", expanded=True):


    st.title("🎬 Amazon Prime Analytics Dashboard")

    st.caption(
        "Interactive Business Intelligence Dashboard powered by Streamlit & Plotly"
    )