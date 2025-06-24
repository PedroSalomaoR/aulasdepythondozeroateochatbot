import os
from langchain_community.document_loaders import WebBaseLoader 
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

#carregando conteúdo do site
loader = WebBaseLoader('https://www.youtube.com/')
documentos = loader.load()

documento = ''
for doc in documentos:
    documento += doc.page_content

#exibir parte do conteúdo carregado
print(documento)

#configurar API Key
api_key = ''
os.environ['GROQ_API_KEY'] = api_key

#iniciar modelo
chat = ChatGroq(model="llama3-70b-8192")

#criar template com mensagens
template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado Salmão e tem acesso às seguintes informações para responder: {documentos_informados}'),
    ('user', '{input}')
])

#criar a chain
chain = template | chat

#fazer pergunta com base nos dados carregados
resposta = chain.invoke({
    'documentos_informados': documento,
    'input': 'Quais são os vídeos disponíveis?'
})

#mostrar resposta
print(resposta.content)
