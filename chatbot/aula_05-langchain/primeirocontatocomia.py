#criando api
api_key=''

#fazendo a primeira chamada ao modelo
import os

os.environ['GROQ_API_KEY'] = api_key

from langchain_groq import ChatGroq

#escolhendo o modelo
chat = ChatGroq(model="llama-3.3-70b-versatile")

#Fazendo uma pergunta para ele
resposta = chat.invoke('Olá, modelo! Quem é você? ')
print(resposta.content)