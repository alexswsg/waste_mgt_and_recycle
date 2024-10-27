# Set up and run this Streamlit App
import streamlit as st
from logics.waste_mgt_query_handler import process_user_query
from helper_functions.utility import check_password, check_for_malicious_intent


# Example usage
if __name__ == "__main__":
    # region <--------- Streamlit App Configuration --------->
    st.set_page_config(
        layout="centered",
        page_title="Waste Management and Recycling"
    )
    # endregion <--------- Streamlit App Configuration --------->

    # Check if the password is correct.  
    if not check_password():  
        st.stop()
    
    st.title("Waste Management and Recycling")
    st.divider()

    
    with st.expander("PLEASE READ DISCLAIMER BEFORE PROCEEDING"):
        st.write(
        """
        IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

        Always consult with qualified professionals for accurate and personalized advice.
        """)

    user_input = st.text_input(label="Ask Question related to waste management and recycling in Singapore")
    submit_button = st.button("Submit!", type='primary')

    preset_option = st.selectbox(
        "Or try one of these prompts!",
        (
        "",
        "how can I dispose used battery properly?",
        "What are the penalties for the illegal disposal of office furniture?",
        "What happens to contaminated recyclables?"
        )
    )

    if preset_option != "":
        print("preset selected")
        with st.spinner("Just a moment, please...."):
            print(f"{preset_option=}")
            result = process_user_query(preset_option)
            print(f"{result=}")
            st.write(result.raw)
    elif submit_button:
        print("user input query")
        check_for_malicious_intent(user_input)
        with st.spinner("Just a moment, please...."):
            print(f"{user_input=}")
            result = process_user_query(user_input)
            print(f"{result=}")
            st.write(result.raw)
        