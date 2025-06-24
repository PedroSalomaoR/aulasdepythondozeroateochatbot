import os
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, YoutubeLoader
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Configurando API KEY
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

# Inicializando modelo
chat = ChatGroq(model="llama3-70b-8192")

# Função principal de resposta do bot
def respostadobot(mensagens, documento):
    mensagem_modelo = [
        ('system', f'Você é um assistente amigável chamado Salmão. Use as seguintes informações para responder: {documento}')
    ]
    mensagem_modelo += mensagens  # Adiciona histórico de conversas
    template = ChatPromptTemplate.from_messages(mensagem_modelo)
    chain = template | chat
    return chain.invoke({}).content

# Carregador de sites
def carrega_site():
    urlsite = input("Digite a URL do site: ")
    loader = WebBaseLoader(urlsite)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

# Carregador de PDF
def carrega_pdf():
    caminho = r"C:\Users\User\OneDrive\Documentos\aulas-python\chatbot\aula_05-langchain\pastaparatestedeacessoempdf\816aa00a-67fd-48c9-9b1b-7767393b461e.pdf"
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

# Carregador de vídeo do YouTube
def carrega_youtube():
    urlyoutube = input("Digite a URL do vídeo do YouTube: ")
    loader = YoutubeLoader.from_youtube_url(
        urlyoutube,
        language=['pt']
    )
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    if not documento:
        print("⚠️ Nenhum conteúdo carregado. O vídeo pode não ter legenda em português.")
    return documento

# Início da aplicação
print("Bem-Vindo(a)! Este é o meu Bot Salmão!")
print("Digite um valor entre 1 e 4")

textoselecao = """
[1] Sites
[2] PDF
[3] Vídeo do YouTube
[4] ChatBot sem contexto
"""

documento = ''
while True:
    print(textoselecao)
    selecao = input("Digite aqui o número: ")

    if selecao == '1':
        documento = carrega_site()
        break
    elif selecao == '2':
        documento = carrega_pdf()
        break
    elif selecao == '3':
        documento = carrega_youtube()
        break
    elif selecao == '4':
        print("ChatBot sem contexto ativado.")
        documento = ''
        break
    else:
        print("❌ Valor inválido. Digite um número entre 1 e 4.")

# Loop de conversa com o bot
mensagens = []
while True:
    pergunta = input("Usuário: ")
    if pergunta.lower() == 'x':
        break
    mensagens.append({'role': 'user', 'content': pergunta})
    resposta = respostadobot(mensagens, documento)
    mensagens.append({'role': 'assistant', 'content': resposta})
    print(f"Bot: {resposta}")

print("Muito obrigado por usar meu Bot!")
print(mensagens)
