from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os


sample_paper = os.path.join(os.path.dirname(__file__), "sample_data", "sample_paper.pdf")
loader = PyPDFLoader(sample_paper)


pages = loader.load_and_split()

# print(pages[46])

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
docs = faiss_index.similarity_search("what is the goal of transformers", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content[:300])