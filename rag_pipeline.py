from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI  # Changed from Groq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Step_1: Setup LLM (Now using Google Gemini)
llm_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Step_2: Retrieve Docs 
def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

# Step_3: Answer Question
custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Don't provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model | StrOutputParser()
    return chain.invoke({"question": query, "context": context})