from dotenv import load_dotenv

import ollama
import requests

from langchain_openai import ChatOpenAI
from langchain_core.documents import Document

load_dotenv()

# llm = ChatOpenAI()
# llm.invoke("Hello, world!")
# documents = [
#     Document(
#         page_content="Dogs are great companions, known for their loyalty and friendliness.",
#         metadata={"source": "mammal-pets-doc"},
#     ),    
#     Document(
#         page_content="Cats are independent pets that often enjoy their own space.",
#         metadata={"source": "mammal-pets-doc"},
#     ),
# ]

response = ollama.generate(model='llama3.2', prompt='what is a qubit?')
print(response['response'])



# URL of the API endpoint
url = 'http://localhost:11434/api/chat'

# JSON data to be sent in the request body
data = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": "why is the sky blue?"
        }
    ]
}

# Set the headers and parameters for the request
headers = {'Content-Type': 'application/json'}

# Send the POST request with JSON data
response = requests.post(url, json=data, headers=headers)

# Check if the response was successful
if response.status_code == 200:
    print('Response from server:', response.json())
else:
    print('Error occurred:', response.status_code)