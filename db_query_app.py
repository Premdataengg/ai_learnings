from langchain import OpenAI, SQLDatabase
from langchain.chains import create_sql_query_chain
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get('OPENAI_API_KEY')
db_pass = os.environ.get("password")
db = os.environ.get('postgres_db')

# Setup database
db = SQLDatabase.from_uri(
    f"postgresql+psycopg2://postgres:{db_pass}@localhost:5432/{db}",
)

# setup llm
llm = OpenAI(temperature=0, openai_api_key=API_KEY)

# Create db chain
QUERY = """
Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
Use the following format:

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
"""

# Setup the database chain
db_chain = create_sql_query_chain(llm=llm, db=db)


def get_prompt():
    print("Type 'exit' to quit")

    while True:
        prompt = input("Enter a prompt: ")

        if prompt.lower() == 'exit':
            print('Exiting...')
            break
        else:
            try:
                # question = QUERY.format(question=prompt)
                print(prompt)
                print(db_chain.invoke(prompt))
            except Exception as e:
                print(e)

get_prompt()