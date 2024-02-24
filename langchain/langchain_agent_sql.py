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
# query_res = db.run("SELECT * FROM Artist LIMIT 10;")
# print(query_res)


#Agent executor
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)


agent_executor.invoke(
    "List the total sales per country. Which country's customers spent the most?"
)