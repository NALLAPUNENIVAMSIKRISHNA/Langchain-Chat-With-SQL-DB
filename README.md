# ChatSQL: Natural Language Database Interaction

Live Demo video :- https://drive.google.com/file/d/1sg52mlRcD4s9YDyAZ7SvhG8EBUsnBU8O/view?usp=sharing

ChatSQL is a Streamlit application that allows you to interact with your SQL databases using natural language. Powered by LangChain and the Groq LLM, it translates your questions into SQL queries, making database interaction simple and intuitive.

## Features

* **Natural Language Queries:** Ask questions in plain English and get results directly from your database.
* **SQLite and MySQL Support:** Connect to local SQLite databases or remote MySQL servers.
* **Interactive Chat Interface:** User-friendly Streamlit interface for seamless interaction.
* **LangChain Integration:** Utilizes LangChain's SQL agent for efficient query translation.
* **Groq LLM Powered:** Uses the fast Groq LLM for quick and accurate responses.
* **Verbose Output:** Shows the steps the LLM is taking to create the SQL query.
* **Clear History:** Ability to clear the chat history.
* **Easy Setup:** Simple configuration for database connections and API keys.

## Getting Started

### Prerequisites

* Python 3.7+
* A Groq API key (We will get from Groq's cloud website)
* For MySQL connections, a MySQL server and credentials.

### Installation

1.  **Clone the repository**

2.  **Create a virtual environment**


3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

### Usage

1.  **Database Selection:**
    * In the sidebar, choose between "Use SQLLITE 3 Database - student.db" or "Connect to your SQL Database."
    * If selecting MySQL, provide the host, user, password, and database name.
2.  **Groq API Key:**
    * Enter your Groq API key in the sidebar.
3.  **Ask Questions:**
    * Use the chat input to ask questions about your database.
4.  **View Results:**
    * The application will display the results of your query in the chat interface.
5.  **Clear History:**
    * Click the "Clear message history" button in the sidebar to reset the chat.

### Code Explanation

* **`app.py`:**
    * This file contains the Streamlit application and the LangChain SQL agent setup.
    * It handles database connections, API key input, and query processing.
    * It uses the Groq LLM to translate natural language into SQL.
* **`sqlite.py`:**
    * This script creates the `student.db` SQLite database and populates it with sample student data.
    * It's used for local testing and demonstration purposes.
* **`student.db`:**
    * This is the local sqlite database created by the sqlite.py script.

### Dependencies

* `streamlit`
* `langchain`
* `sqlalchemy`
* `sqlite3`
* `mysql-connector-python` (for MySQL)
* `langchain-groq`
