# Criando uma chain com LangChain e Groq
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

#configurando API KEY
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

#inicializando modelo
chat = ChatGroq(model="llama3-70b-8192")

#criando o prompt template
#podemos criar mais de um template
template = ChatPromptTemplate.from_messages([
    {'role': 'user', 'content': 'Traduza {expressao} para a língua {lingua}'}
])

#formatando as mensagens
mensagens = template.format_messages(expressao='beleza?', lingua='inglesa')

#exibindo mensagens formatadas
for msg in mensagens:
    print(f"{type(msg).__name__}: {msg.content}")

#criando a chain (template -> modelo)
chain = template | chat

#chamando a chain com os dados corretos
resposta = chain.invoke({'expressao': 'beleza?', 'lingua': 'inglesa'})

#mostrando a resposta
print("Resposta do modelo:", resposta.content)
