from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
response = llm(messages=[
    {"role": "user", "content": "Print an IB Physics IA topic for a student who is interested in astronomy and astrophysics."}
])
print(response