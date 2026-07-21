import streamlit as st
import pandas as pd 

from utils import clean_data 
from utils import parse_list_column


st.set_page_config(
    page_title="📊 AI-Powered Business Intelligence Dashboard",
    layout="wide"
)

st.title("📊 AI-Powered Business Intelligence Dashboard")
# st.write("Upload a dataset and analyze it.")

# upload data 
uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)
# st.title("📊 AI-Powered Business Intelligence Dashboard")

# uploaded_file = st.file_uploader(
#     "Upload Amazon Prime Titles CSV",
#     type=["csv"]
# )

if uploaded_file is None:
    st.info("👆 Please upload the Amazon Prime Titles dataset to start the analysis.")
    st.stop()

# # Read the uploaded file
df = pd.read_csv(uploaded_file)

# # Clean the data
# df = clean_data(df)

# # #  displaying the data overview
# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     df = clean_data(df)

# adding sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dataset Overview",
        "Visualizations",
        "KPIs",
        "AI Analyst"
    ]
)

if page == "Dataset Overview":

    st.header("Dataset Overview")
    st.dataframe(df.head(10))

    st.subheader("Data Types")
    st.dataframe(df.dtypes.astype(str))

    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum())


# Apply filters
from filters import apply_filters
filtered_df = apply_filters(df)
 
   
# adding kpis
from kpi import *
if page == "KPIs":

    show_kpis(filtered_df)

    dataset_summary(filtered_df)

    content_insights(filtered_df)

    rating_insights(filtered_df)

    runtime_insights(filtered_df)

    genre_insights(filtered_df)

    country_insights(filtered_df)

    quality_report(filtered_df)

# page dashboard
from dashboard import show_dashboard
if page == "Visualizations":
    show_dashboard(filtered_df)

# page Ai analysis
from ai_app import show_ai_page
if page == "AI Analyst":
    show_ai_page(filtered_df)


