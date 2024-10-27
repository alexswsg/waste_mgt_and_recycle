import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Project Scope and Documentation for Waste Management & Recycling Query System")

st.write("""


## **1. Project Overview**  
This project aims to build a **smart query system** that helps users find accurate and up-to-date information on **waste management and recycling in Singapore**. It integrates both **natural language processing (NLP)** and SQL-based analysis to respond to user queries with insights from authoritative sources and structured datasets. 

### **Purpose**  
- Empower users to access waste management guidelines, recycling data, and trends effortlessly.  
- Provide concise, relevant responses aligned with **Singapore’s public communication standards**.  
- Use NLP to transform user queries into **actionable SQL queries** that extract meaningful insights from a structured recycling dataset.  

---

## **2. Objectives**  
1. **User Query Analysis:** Identify and classify the intent behind user questions (e.g., disposal, penalties, recycling trends).
2. **Dynamic Research and Response:** Retrieve **Singapore-specific waste management information** from trusted sources (e.g., NEA, Zero Waste SG).  
3. **Data-driven Insights:** Use SQL to query a **recycling dataset** and provide detailed visualizations (e.g., bar charts) when relevant.  
4. **Friendly Communication:** Ensure responses align with **public-friendly tone** and encourage **sustainable practices**.

---

## **3. Scope**  
This project consists of two key components:  
1. **Waste Management Query System**  
   - Uses **multiple agents** to analyze user queries and gather up-to-date data from NEA and other sources.  
   - Provides short, **clear, and helpful responses** for waste disposal and recycling-related inquiries.  

2. **Recycling Data Analysis System**  
   - Uses **NLP and SQL agents** to interpret queries and generate relevant SQL queries based on a **schema-defined recycling dataset**.  
   - Provides **visualized insights** through **charts** on recycling trends.

---

## **4. Data Sources**  
The system pulls information from several official and trusted sources:

1. **National Environment Agency (NEA):**  
   - Services: [NEA Waste Management](https://www.nea.gov.sg/our-services/waste-management/)  
   - News: [NEA News](https://www.nea.gov.sg/media/news)  

2. **Zero Waste SG:**  
   - Information on **zero waste initiatives** in Singapore: [Zero Waste SG](https://www.zerowastesg.com/)  

3. **Recycling Dataset [Recycling Rate By Waste Type](https://data.gov.sg/datasets?query=waste&page=1&resultId=d_9740df787da2b59a0b5bd76a6c33453d):**  
   - Historical data on **recycling rates** by waste type (2000-2015).
   - Stored in an SQLite database for **SQL-based analysis**.

---

## **5. System Features and Architecture**

### **A. Waste Management Query System**  
- **Agents:**
  - **Query Analyzer Agent:** Identifies the intent and focus of user queries (e.g., disposal methods, recycling penalties).  
  - **Research Agent:** Pulls relevant guidelines and articles from NEA and Zero Waste SG.  
  - **Response Generator Agent:** Generates friendly, **concise answers** based on research findings.  

- **Process:**
  - Accepts **text inputs** from users or provides **preset questions** for convenience.
  - Asynchronously analyzes and researches **Singapore-specific policies**.

#### **Example Queries:**
- *“How do I dispose of used batteries?”*  
- *“What are the penalties for illegal furniture disposal?”*  
- *“What happens to contaminated recyclables?”*  

---

### **B. Recycling Data Analysis System**  
- **Agents:**  
  - **NLP Agent:** Interprets **user queries** and extracts relevant parameters (e.g., year, waste type) based on the **recycling schema**.  
  - **SQL Agent:** Generates **optimized SQL queries** to extract data within schema constraints.  

- **Process:**
  1. User provides a query (e.g., “How has plastic recycling changed over the past 5 years?”).
  2. The NLP agent processes the query and passes parameters to the SQL agent.
  3. The SQL agent executes queries against the SQLite **recycling dataset** and returns results.
  4. Results are visualized using **bar charts** in Streamlit.

#### **Example Queries:**
- *“What is the highest recycling rate waste type in 2011?”*  
- *“Which waste types improved the most over the past decade?”*  

---

## **6. Technology Stack**

- **Frontend Interface:**  
  - **Streamlit:** For user interaction, input forms, and chart generation.
  
- **Backend Components:**  
  - **Python Agents:** Manage NLP, SQL queries, and data analysis.  
  - **SQLite Database:** Stores the recycling data.  
  - **OpenAI API:** Used to process user input with language models.  

- **Data Handling:**  
  - **Schema:** Constraints ensure the **validity of SQL queries** (e.g., years limited to 2000-2015).
  - **Chart Visualization:** Displays SQL results through **bar charts** in Streamlit.  

---

## **7. Flow and Interaction**

### **1. Waste Management Queries:**  
1. User submits a query via the interface (or selects a preset).  
2. **Query Analyzer Agent** identifies the intent.  
3. **Research Agent** gathers guidelines and facts from NEA or Zero Waste SG.  
4. **Response Generator Agent** creates a concise, **public-friendly reply.**

### **2. Recycling Data Queries:**  
1. User inputs a natural language query related to recycling trends.  
2. **NLP Agent** interprets the input and passes parameters to the **SQL Agent**.  
3. SQL Agent retrieves data from the **SQLite database**.  
4. The results are displayed as a **chart** or summary in Streamlit.

---

## **8. Key Benefits and Outcomes**

1. **User-Friendly Interface:** Simple and interactive experience for non-technical users.  
2. **Accurate Information:** Ensures all guidelines follow **Singapore’s policies and regulations**.  
3. **Visual Insights:** Provides meaningful recycling trends using **dynamic visualizations**.  
4. **Scalable Design:** Modular architecture makes it easy to extend features in the future.

---

## **9. Example User Interface Screenshots**

### Waste Management Query Interface:
- **Title:** "Waste Management and Recycling"
- **Text Input Box:** For user queries related to **waste management**.
- **Preset Options:** Quick prompts to explore common queries (e.g., “How to dispose of batteries?”).

### Recycling Data Analysis Interface:
- **Title:** "Dataset about Recycling Rate By Waste Type"
- **Preset Options:** Questions to explore **trends** (e.g., “Which waste type had the highest rate in 2011?”).
- **Bar Chart:** Visualization of recycling trends.

---

## **10. Conclusion**  
This project combines **machine intelligence and data analysis** to provide quick, accurate answers about **waste management and recycling** in Singapore. It simplifies **access to information** while offering **insights through data visualizations**, fostering more sustainable behaviors and informed decision-making.  

This solution can easily scale by integrating additional datasets or expanding **language models** for better NLP performance in future updates.

""")

