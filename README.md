# llm-text-to-sql-agent
Text-to-SQL analyst: ask a business question in plain English, and a Groq-hosted LLM writes the SQL, a read-only guardrail checks it, and Snowflake runs it. Failed queries go back to the LLM for one retry with the error. Built in Python with a Streamlit UI over Snowflake's TPC-H sample data.
