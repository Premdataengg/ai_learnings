from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

output = llm.invoke("tell me a joke")
print(output)

output = llm.invoke("write python code to import a file from ftp for airflow")
print(output)

