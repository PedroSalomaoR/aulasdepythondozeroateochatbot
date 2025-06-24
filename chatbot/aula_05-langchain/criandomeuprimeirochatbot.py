import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

#configurando API KEY
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

#inicializando modelo
chat = ChatGroq(model="llama3-70b-8192")

def respostadobot(mensagens):
    mensagem_modelo = [('system', 'Você é um assistente amigável chamado Salmão')]
    mensagem_modelo += mensagens #soma os históricos das conversas
    template = ChatPromptTemplate.from_messages(mensagem_modelo)
    chain = template | chat
    return chain.invoke({}).content

print("Bem-Vindo(a)! Este é o meu Bot Salmão!")
mensagens = []
while True:
    pergunta = input("Usuario: ")
    if pergunta.lower() == 'x':
        break
    mensagens.append({'role': 'user', 'content': pergunta})
    resposta=respostadobot(mensagens)
    mensagens.append({'role': 'assistant', 'content': resposta})
    print(f"Bot: {resposta}")
    
print("Muito obrigado por usar meu Bot!")
print(mensagens)