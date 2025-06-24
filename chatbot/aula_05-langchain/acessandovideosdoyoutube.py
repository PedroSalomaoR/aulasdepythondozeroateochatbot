#foi necessário instalar o yt-dlp , -U langchain langchain-community e o youtube-transcript-api
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader
from langchain.prompts import ChatPromptTemplate

#configurando API KEY
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

#inicializando modelo
chat = ChatGroq(model="llama3-70b-8192")

#youtube
url = 'https://www.youtube.com/watch?v=Q2f7yyDRCO8'
loader = YoutubeLoader.from_youtube_url(
    url,
    language=['pt']  # vai buscar legendas em português
)

lista_documentos = loader.load()

if not lista_documentos:
    print("⚠️ Nenhum conteúdo carregado. O vídeo pode não ter legenda em português.")
else:
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    print(documento[:1000]) #limitador
    
template = ChatPromptTemplate.from_messages([
    ('system','Você é um assistente amigável chamado salmão, que possui as seguintes informações para formular uma resposta: {informacoes}'),
    ('user' , '{input}')
])    

chain_youtube = template | chat
resposta = chain_youtube.invoke({'informacoes':documento, 'input':'Quais eram os times do vídeo?'})
print(resposta.content)
