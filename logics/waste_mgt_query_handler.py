import asyncio
from dotenv import load_dotenv
import requests
# Import the key CrewAI classes
from crewai import Agent, Task, Crew

# import other necessary packages you need

from crewai_tools import WebsiteSearchTool



# Initialize search tools specific to waste management in Singapore
web_search_tool_nea_waste_mgt = WebsiteSearchTool(
    "https://www.nea.gov.sg/our-services/waste-management/"
)
web_search_tool_nea_news = WebsiteSearchTool(
    "https://www.nea.gov.sg/media/news"
)
web_search_tool_zero_waste_sg = WebsiteSearchTool(
    "https://www.zerowastesg.com/"
)

def process_user_query(user_query):
    # Creating Agents
    agent_query_analyzer = Agent(
        role="Query Analyzer",
        goal="Identify the specific waste management issue within the user query: {user_query}",
        backstory="""You work on analyzing the user's question to determine what area of waste management the query focuses on. 
        This helps ensure that research and responses are targeted effectively.""",
        allow_delegation=False,
        verbose=True,
    )

    agent_researcher = Agent(
        role="Waste Management Researcher",
        goal="Gather relevant, up-to-date data and guidelines based on the user query: {user_query}",
        backstory="""You use official sources to gather accurate and updated information on waste management based on the query.
        Your task is to ensure the information is locally relevant, focusing on Singapore's waste management policies.""",
        allow_delegation=False,
        verbose=True,
    )

    agent_response_generator = Agent(
        role="Response Generator",
        goal="Generate a short, friendly, and helpful response addressing the user's query: {user_query}",
        backstory="""Based on the research provided, you generate an answer that is easy to understand, friendly, and concise, ensuring 
        it aligns with the tone of public communication in Singapore.""",
        allow_delegation=False,
        verbose=True,
    )

    # Creating Tasks
    task_analyze_query = Task(
        description="""\
        1. Identify the key focus of the user query: {user_query} (e.g., disposal methods, recycling, or awareness).
        2. Determine whether the query involves residential, commercial, or special waste like PPE.
        3. Provide the identified focus to the Waste Management Researcher to aid targeted research.""",
        expected_output="A summary of the key focus identified in the user query.",
        agent=agent_query_analyzer,
        # async_execution=True
    )

    task_research = Task(
        description="""\
        1. Use identified focus from Query Analyzer to find relevant data and guidelines from NEA, MSE, and Zero Waste SG.
        2. Ensure research addresses local policies, best practices, and solutions relevant to the user query.
        3. Provide insights to the Response Generator, ensuring clarity and factual accuracy.""",
        expected_output="A concise research summary with Singapore-specific data and guidelines.",
        agent=agent_researcher,
        tools=[web_search_tool_nea_waste_mgt, web_search_tool_nea_news, web_search_tool_zero_waste_sg],
        # async_execution=True
    )

    task_generate_response = Task(
        description="""\
        1. Use the research summary to generate a concise, friendly response (not more than 150 words or 5 sentences).
        2. Ensure the tone is approachable and encourages sustainable practices.
        3. Proofread for accuracy and readability to align with public communication standards.""",
        expected_output="A friendly and concise response addressing the user's query.",
        agent=agent_response_generator,
        context=[task_analyze_query, task_research]

    )

    # Create the Crew
    crew = Crew(
        agents=[agent_query_analyzer, agent_researcher, agent_response_generator],
        tasks=[task_analyze_query, task_research, task_generate_response],
        verbose=True
    )

    return crew.kickoff(inputs={"user_query":user_query})