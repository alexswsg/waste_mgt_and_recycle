import json
import sqlite3
import pandas as pd
import streamlit as st
from logics.recycling_waste_handler import analyse_recycling_data
from helper_functions.utility import generate_list
from helper_functions.utility import check_password, check_for_malicious_intent

def generate_chart(user_query):
    st.write(user_query)
    st.divider()

    result = analyse_recycling_data(user_query)
    print(f"{result.raw=}")

    # # Extract outputs

    sql_query_output = result.raw
 
    
    with sqlite3.connect('db/recycling_records.db') as connection:
        result = connection.execute(sql_query_output).fetchall()
        print(f"{result=}")

    if len(result) == 1:
        st.write(result)
    else:
        return_chart_data = generate_list(sql_query_output, result)
        print("@"*20)
        print(f"{return_chart_data=}")
        json_chart_data = json.loads(return_chart_data)
        print(json_chart_data["data"])
        chart_data = pd.DataFrame(data=json_chart_data["data"])

        st.bar_chart(chart_data, x= json_chart_data["x"],y=json_chart_data["y"])

# Example usage
if __name__ == "__main__":
    st.title("Dataset about Recycling Rate By Waste Type")
    st.divider()
    if not check_password():  
        st.stop()
    
    with st.expander("PLEASE READ DISCLAIMER BEFORE PROCEEDING"):
        st.write(
        """
        IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

        Always consult with qualified professionals for accurate and personalized advice.
        """)

user_input = st.text_input(label="Ask Question related to recycling and waste management in Singapore")
submit_button = st.button("Submit!", type='primary')

preset_option = st.selectbox(
    "Or try one of these prompts!",
    (
    "",
    "Which waste type has the highest rate in 2011?",
    "How has the recycling rate for plastics changed over the last 5 years?",
    "What is the average recycling rate for each waste type across all years?",
    "Comparison of recycling rates across different waste types for a 2010",
    "What is the current recycling rate for food waste, and how has it changed in recent years?",
    "Which types of waste have shown the most significant improvement in recycling rates over the past decade?"
     )
)

if preset_option != "":
    print("preset selected")
    with st.spinner("Just a moment, please...."):
        generate_chart(preset_option)
elif submit_button:
    print("user input query")
    check_for_malicious_intent(user_input)
    with st.spinner("Just a moment, please...."):
        st.write(generate_chart(user_input))
      
