import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
from ai_summary import *
from dashboard_summary import create_dashboard_summary
load_dotenv()
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)
# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )


def ask_ai(question, dataframe):

    # Small sample of the filtered dataset
    # sample = dataframe.head(15).to_string(index=False)

    summary = get_dataset_summary(dataframe)

    genres = top_genres(dataframe)

    countries = top_countries(dataframe)
    dashboard = create_dashboard_summary(dataframe)
    prompt = f"""
You are a Senior Business Data Analyst.

Current Dashboard Summary

{dashboard}

User Question

{question}

Instructions

- Answer only using the dashboard summary.
- Give business insights.
- Explain trends.
- Mention important observations.
- Suggest recommendations.
"""
#     prompt = f"""
# You are a Senior Data Analyst.

# Dataset Statistics

# {summary}

# T"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a senior business data analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3

    )

    return response.choices[0].message.content