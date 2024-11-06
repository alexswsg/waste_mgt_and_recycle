import json
from crewai import Agent, Task, Crew, Process
import streamlit as st
from openai import OpenAI
from langchain_openai import ChatOpenAI


OPENAI_KEY = st.secrets['OPENAI_API_KEY']
OPENAI_MODEL = st.secrets['OPENAI_MODEL_NAME']
OPENAI_TEMPERATURE = float(st.secrets['TEMPERATURE'])


# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=OPENAI_KEY)

manager_llm = ChatOpenAI(model_name=OPENAI_MODEL, api_key=OPENAI_KEY, temperature=OPENAI_TEMPERATURE)

# Load the schema information from the JSON file
with open('./schema/recycling.json', 'r') as file:
    schema_info = json.load(file)
# print(f"{schema_info=}")
# Natural Language Processor Agent
nlp_agent = Agent(
    role='Natural Language Processor',
    goal="""Interpret the following natural language input about recycling data: 
            {user_query}
            Use the following schema: 
            {schema_info}
            Ensure the constraints in {schema_info} are respected.""",

    verbose=False,
    memory=True,
    allow_delegation=False,
    backstory=(
        "You are skilled at understanding and interpreting natural language queries about recycling data to align them with schema constraints. "
        "Your goal is to extract the relevant information needed to form a SQL query."
    ),
    max_iter=5,
)

# SQL Generator Agent
sql_agent = Agent(
    role='SQL Generator',
    goal="""Generate SQL queries based on the user input: {user_query}.
            Ensure the query aligns with the schema constraints: {schema_info}.
            If the requested year range is the schema constraints (years 2000 to 2015), 
            adjust it accordingly. Do not query out of schema constraints.
            Always limit the SQL query to {n_rows} rows.""",
    verbose=False,
    memory=True,
    allow_delegation=False,    
    backstory=(
        "You are an expert in SQL query formation, particularly for recycling data analysis."
        "Your goal is to generate accurate and optimized SQL queries based on structured data that comply with schema constraints."
    ),
    max_iter=5,
)

# Task for interpreting natural language
interpret_nl_task = Task(
    description=(
        """Interpret the following given natural language input about recycling data: 
           {user_query} 
           Extract intent and parameters.
           Use the following schema: 
           {schema_info}"""
    ),
    expected_output="A dictionary with 'intent' and 'parameters'.",
    agent=nlp_agent,
)

# Task for generating SQL query
generate_sql_task = Task(
    description=(
        """Generate SQL queries based on the following natural language input about recycling data: 
           {user_query} 
           Consider the following schema in your analysis:
           {schema_info}
        Your final answer MUST be a valid and optimized SQL query string.
        Always limit this SQL query to {n_rows} rows. """
    ),
    expected_output="A valid and optimized SQL query string without markup",
    agent=sql_agent,
)


    
# Function to run the crew with a user query
def analyse_recycling_data(user_query, n_rows=50):

    # Define the manager agent
    recycling_data_manager = Agent(
        role="Recycling Data Analysis Manager",
        goal="""Oversee the process of interpreting natural language queries about recycling data, 
                generating SQL queries, and analysing the results.
                Your final response should include the SQL query and a summary of the recycling trends analysis.""",
        verbose=False,
        memory=True,
        backstory=(
            "You are an experienced manager with expertise in recycling data analysis. "
            "Your goal is to coordinate the process of transforming user queries into actionable insights about recycling trends."
        ),
        allow_delegation=True,
        llm=manager_llm,
        tools=[],
        max_iter=5,
    )
    
    # Creating the crew with all agents and tasks
    recycling_analysis_crew = Crew(
        agents=[nlp_agent, sql_agent],
        tasks=[interpret_nl_task, generate_sql_task],
        manager_agent=recycling_data_manager,
        process=Process.hierarchical,
        manager_llm=manager_llm,
    )


    input_data = {
        'user_query': user_query,
        'schema_info': schema_info,
        'n_rows': n_rows
    }
    print(20*"#")
    print(f"{recycling_data_manager.tools=}")
    result = recycling_analysis_crew.kickoff(inputs=input_data)
    return result

