# ai_page.py
import streamlit as st
from llm import ask_ai
from prompts import SUGGESTED_PROMPTS
from report import generate_report
from suggestions import SUGGESTIONS


def show_ai_page(filtered_df):

    st.title("🤖 AI Data Analyst")

    # ============================================
    # Initialize Chat History
    # ============================================
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ============================================
    # Clear Chat
    # ============================================
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    # ============================================
    # Display Chat History
    # ============================================
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.divider()

    # ============================================
    # Quick AI Analysis
    # ============================================
    st.subheader("🚀 Quick AI Analysis")

    cols = st.columns(2)

    for i, (title, prompt) in enumerate(SUGGESTED_PROMPTS.items()):

        with cols[i % 2]:

            if st.button(title, key=f"quick_{i}"):

                # Save user prompt
                st.session_state.messages.append({
                    "role": "user",
                    "content": prompt
                })

                # Get AI response
                with st.spinner("🤖 AI is analyzing..."):
                    answer = ask_ai(prompt, filtered_df)

                # Save AI response
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                st.rerun()

    st.divider()

    # Ai Suggetions
    st.divider()

    st.subheader("💡 AI Suggestions")
    selected = st.selectbox(

        "Choose a suggestion",

        SUGGESTIONS
    )

    if st.button("Run Suggestion"):

        answer = ask_ai(
            selected,
            filtered_df
        )

        st.write(answer)
    # ============================================
    # Custom Question
    # ============================================
    question = st.chat_input("💬 Ask anything about the dataset...")

    if question:

        # Save user question
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # Get AI response
        with st.spinner("🤖 AI is analyzing..."):
            answer = ask_ai(question, filtered_df)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()

    # ============================================
# AI Report Generator
# ============================================

    st.divider()
    st.subheader("📄 AI Report Generator")

    # Initialize report storage
    if "report" not in st.session_state:
        st.session_state.report = None

    # Generate report
    if st.button("📄 Generate Business Report"):

        with st.spinner("Generating report..."):

            st.session_state.report = generate_report(filtered_df)

    # Display report if available
    if st.session_state.report:

        st.markdown(st.session_state.report)

        st.download_button(
        label="📥 Download Report",
        data=st.session_state.report,
        file_name="Business_Report.txt",
        mime="text/plain"
    )

