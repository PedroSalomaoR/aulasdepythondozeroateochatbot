#para isto sera necessario instalar o pypdf
import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
#configurando API KEY
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

#inicializando modelo
chat = ChatGroq(model="llama3-70b-8192")

#caminho do pdf
caminho = r"C:\Users\User\OneDrive\Documentos\aulas-python\chatbot\aula_05-langchain\pastaparatestedeacessoempdf\816aa00a-67fd-48c9-9b1b-7767393b461e.pdf"
loader=PyPDFLoader(caminho)
lista_documentos = loader.load()

documento = ''
for doc in lista_documentos:
    documento = documento + doc.page_content
    
template = ChatPromptTemplate.from_messages([
    ('system','Você é um assistente amigável chamado salmão, que possui as seguintes informações para formular uma resposta: {informacoes}'),
    ('user' , '{input}')
])    

chain_pdf = template | chat
resposta = chain_pdf.invoke({'informacoes':documento, 'input':'O que está escrito na primeira pagina do pdf ?'})
print(resposta.content)
    