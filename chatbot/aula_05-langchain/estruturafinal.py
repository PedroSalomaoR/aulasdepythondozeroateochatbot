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

def carrega_site():
    urlsite=input("Digite a url do site: ")
    documento = ' '
    return documento

def carrega_pdf():
    documento = ' '
    return documento

def carrega_youtube():
    urlyoutube=input("Digite a url do vídeo: ")
    documento = ' '
    return documento

print("Bem-Vindo(a)! Este é o meu Bot Salmão!")

print("Digite um valor entre 1 e 4")

textoselecao = """
[1] Sites
[2] PDF
[3] Vídeo do YouTube
[4] ChatBot
"""

while True:
    print(textoselecao)
    selecao = input("Digite aqui o número: ")
    
    if selecao == '1':
        documento = carrega_site()
        break
    elif selecao == '2':
        print("PDF")
        documento = carrega_pdf()
        break
    elif selecao == '3':
        print("Vídeo do Youtube")
        documento = carrega_youtube()
        break
    elif selecao == '4':
        print("ChatBot")
        break
    else:
        print("❌ Valor inválido. Digite um número entre 1 e 4.")


    
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