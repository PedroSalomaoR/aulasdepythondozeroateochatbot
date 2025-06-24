from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    {'role': 'user', 'content': 'Traduza {expressao} para a língua {lingua}'}
])

mensagens = template.format_messages(expressao='beleza?', lingua='inglesa')

for msg in mensagens:
    print(f"{type(msg).__name__}: {msg.content}")
