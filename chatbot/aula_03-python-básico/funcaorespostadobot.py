#teste para função de resposta do bot
def respostadobot(mensagem):
    return "Resposta do bot"

print("Bem-Vindo(a)! Este é o meu Bot!")
mensagens = []
while True:
    pergunta = input("Usuario: ")
    if pergunta.lower() == 'x':
        break
    mensagens.append({'role':'user', 'content': pergunta})
    resposta=respostadobot(mensagens)
    mensagens.append({'role':'assistant', 'content': resposta})
    print(f"Bot: {resposta}")
    
print("Muito obrigado por usar meu bot!")
print(mensagens)    