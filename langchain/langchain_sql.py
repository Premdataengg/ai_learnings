import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.agent_toolkits import create_sql_agent
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough


load_dotenv()
API_KEY = os.environ.get('OPENAI_API_KEY')
# print(API_KEY)

#database conenction test
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
# print(db.dialect)
# print(db.get_usable_table_names())
query_res = db.run("SELECT * FROM Artist LIMIT 10;")
# print(query_res)

# Convert question to SQL query
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

write_query = create_sql_query_chain(llm, db)
execute_query = QuerySQLDataBaseTool(db=db)
chain = write_query | execute_query
res = chain.invoke({"question": "How many employees are there"})
# print(res)

#Now that we’ve got a way to automatically generate and execute queries, we just need to combine the original question
# and SQL query result to generate a final answer. We can do this by passing question and result to the LLM once more:
answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)

answer = answer_prompt | llm | StrOutputParser()
chain = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | execute_query
    )
    | answer
)
#How many employees are born before 1950
#give me the hiredates of each employee with names and format date in mm-dd-yyyy

res = chain.invoke({"question": "give me the total amount per customer and format the output "})
# git(res)



#sql agent
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

agent_executor.invoke(
    {
        "input": "List the total sales per country. Which country's customers spent the most?"
    }
)

agent_executor.invoke({"input": "how many tables have column that contains the word Id print the table names and column names"})