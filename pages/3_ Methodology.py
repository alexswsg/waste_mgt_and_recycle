import streamlit_mermaid as stmd
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Methodology"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

st.write("""
# **Comprehensive Explanation of Data Flows and Implementation Details**
## 1. User Query for Waste Management and Recycling
### **1.1. Overview of the Application Design**
This application facilitates **waste management and recycling-related queries** using a **multi-agent system** that interacts with official sources such as the **National Environment Agency (NEA)** and **Zero Waste SG**. It comprises three agents:
1. **Query Analyzer Agent:** Identifies the focus of the user’s query.
2. **Research Agent:** Gathers information from trusted Singapore-based sources.
3. **Response Generator Agent:** Produces concise and friendly responses.

The workflow is designed to ensure **accuracy, relevance, and user-friendliness** in responding to public inquiries about Singapore’s waste management policies and practices.

---

### **1.2. Data Flow Details**

### **A. Initialization of Search Tools**
- **WebsiteSearchTool instances** are created to query:
  - NEA Waste Management services: `https://www.nea.gov.sg/our-services/waste-management/`
  - NEA News: `https://www.nea.gov.sg/media/news`
  - Zero Waste SG: `https://www.zerowastesg.com/`

#### **B. Process Flow for User Queries**
1. **User Input Handling:**
   - Users can **manually enter a query** or **select a preset prompt**.
   - User input is validated to prevent **malicious intent**.

2. **Query Analysis (Agent 1):**
   - The **Query Analyzer Agent** identifies the primary focus of the query (e.g., disposal methods or penalties).  
   - It determines whether the issue concerns **residential, commercial, or special waste** (e.g., PPE).

3. **Research Execution (Agent 2):**
   - The **Research Agent** queries relevant NEA and Zero Waste SG resources to find local policies and best practices.  
   - The gathered data is compiled into a **summary report** for further processing.

4. **Response Generation (Agent 3):**
   - The **Response Generator Agent** uses the research summary to **generate concise responses** (maximum 5 sentences).  
   - The response is designed to align with **public communication standards** and encourage sustainable practices.

5. **Display in Streamlit:**
   - The user receives the final response in the **Streamlit interface**.  
   - If additional prompts or queries are required, users can re-engage with the system.

---

### **1.3. Implementation Details**

#### **A. Multi-Agent Design**  
- **Agent 1: Query Analyzer**  
  - Goal: Analyze the user’s query and extract the primary focus area.  
  - Backstory: Helps streamline research by targeting relevant issues.  

- **Agent 2: Researcher**  
  - Goal: Retrieve accurate, updated data from official sources like NEA and Zero Waste SG.  
  - Tools: Uses pre-configured **WebsiteSearchTool** instances to access specific data sources.

- **Agent 3: Response Generator**  
  - Goal: Craft a friendly and informative response that aligns with the tone of public communication in Singapore.  
  - Context: Uses insights from the **Query Analyzer and Researcher agents** to generate responses.

#### **B. Task Management with Crew Coordination**  
- **Crew** coordinates all agents, ensuring tasks are completed sequentially:
  1. **Task 1: Analyze Query**
     - Extracts the query’s intent and context.
  2. **Task 2: Conduct Research**
     - Gathers data relevant to the identified focus.
  3. **Task 3: Generate Response**
     - Produces a concise and friendly response for the user.

---

### **1.4. Flowchart Illustrating the Process Flow**

#### **A. High-Level Process Flow**
Note: *Scroll on the chart up or down to see complete flowchart*

         """)


code = """
flowchart TD
    A[User Input] --> B[Query Analyzer Agent]
    B --> C[Identify Focus: Disposal/Recycling]
    C --> D[Research Agent]
    D --> E[Search NEA and Zero Waste SG]
    E --> F[Response Generator Agent]
    F --> G[Generate Friendly Response]
    G --> H[Display Response in Streamlit]
"""

stmd.st_mermaid(code)

st.write("""
         #### **B. Detailed Flow for Use Case: User Query Handling**
         Note: *Scroll on the chart up or down to see complete flowchart*
        
         """)

code = """
flowchart TD
    A[User Input: Query or Preset] --> B[Validate Input]
    B -->|Valid Query| C[Analyze Intent]
    C --> D[Research Singapore-Specific Data]
    D --> E[Generate Response]
    E --> F[Display in Streamlit]
    B -->|Invalid Query| G[Error Handling: Display Warning]
"""

stmd.st_mermaid(code)

st.write("""
## 2. Text to SQL for Recycling Rate By Waste Type

### **2.1. Overview of the Application Design**
This code implements a **data analysis application for recycling trends**, using **multi-agent systems** and **SQL query generation**. The goal is to transform **natural language queries** into **SQL queries** that retrieve relevant data from a **recycling database** and display the results in **charts**. The system ensures that user queries align with schema constraints, generating actionable insights.

---

### **2.2. Data Flow Details**

#### **A. Initialization and API Configuration**
- **OpenAI API** is configured using the provided API key for the **language models (LLM)**.
- The **recycling data schema** is loaded from a JSON file (`recycling.json`) to inform both **query interpretation** and **SQL generation**.

#### **B. Workflow for User Queries**
1. **User Input Handling:**
   - Users can enter custom queries or select **preset prompts** about recycling trends.
   - Input is validated for **malicious content** before processing.

2. **Natural Language Processing (NLP Agent):**
   - Interprets the user query and extracts **intent and parameters** based on the schema.

3. **SQL Query Generation (SQL Agent):**
   - Uses the extracted intent and parameters to generate **SQL queries** that align with schema constraints (e.g., year ranges between 2000-2015).
   - Limits SQL queries to **a specific number of rows** to optimize performance.

4. **Database Query Execution:**
   - The generated SQL query is executed on a **SQLite database** containing recycling records.

5. **Result Visualization:**
   - The results are converted into **charts** and displayed in **Streamlit**.

---

### **2.3. Implementation Details**

#### **A. Agents Involved**
- **NLP Agent:**
  - Role: Interprets the user’s natural language input.
  - Goal: Extract **intent and parameters** according to schema rules.

- **SQL Agent:**
  - Role: Generates optimized SQL queries based on user input and schema constraints.
  - Goal: Ensure that the SQL queries **comply with schema limits** and retrieve only relevant data.

- **Manager Agent:**
  - Role: Oversees the entire process from **query interpretation to data analysis**.
  - Goal: Ensure **correct coordination** among the agents and present results effectively.

#### **B. Task Management with Crew Coordination**
- **Task 1: Interpret Natural Language Query**
  - Agent: NLP Agent
  - Output: Dictionary with query **intent and parameters**.

- **Task 2: Generate SQL Query**
  - Agent: SQL Agent
  - Output: **SQL query string** aligned with the schema.

- **Crew Management:**
  - Uses the **hierarchical process** to ensure that tasks flow sequentially from query interpretation to SQL generation and result visualization.

---

### **2.4. Flowchart Illustrating the Process Flow**

#### **A. High-Level Process Flow**
Note: *Scroll on the chart up or down to see complete flowchart*

         """)

code = """
flowchart TD
    A[User Input] --> B[NLP Agent: Interpret Query]
    B --> C[Extract Intent & Parameters]
    C --> D[SQL Agent: Generate SQL Query]
    D --> E[Execute SQL on SQLite DB]
    E --> F[Display Results in Chart]
"""

stmd.st_mermaid(code)

st.write("""
         #### **B. Detailed Flow for Use Case: Preset Query Execution**
         Note: *Scroll on the chart up or down to see complete flowchart*
        
         """)

code = """
flowchart TD
    A[User selects preset prompt] --> B[Generate SQL Query]
    B --> C[Run Query on SQLite Database]
    C --> D[Check Results]
    D -->|Multiple Results| E[Generate Bar Chart]
    D -->|Single Result| F[Display Result Directly]
"""

stmd.st_mermaid(code)