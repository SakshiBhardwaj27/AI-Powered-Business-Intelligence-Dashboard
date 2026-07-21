from llm import ask_ai

def generate_report(df):

    prompt = """
    Create a professional business report using the current dashboard.

    Include:

    1. Executive Summary

    2. Dataset Overview

    3. Key Insights

    4. Trends

    5. Risks

    6. Opportunities

    7. Recommendations

    8. Conclusion

    Write professionally like a Senior Data Analyst.
    """

    return ask_ai(prompt, df)