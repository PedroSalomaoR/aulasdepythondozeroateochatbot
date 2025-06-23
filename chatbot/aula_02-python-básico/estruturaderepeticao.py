#Aula de estruturas de repetição

#While
jogodarepeticao = str(input("Digite X para sair: "))

while jogodarepeticao.lower() != 'x':
    print("O jogo está continuando") 
    jogodarepeticao = input("Digite X para sair: ")

#for 
for i in range(1,6):
    print("numero:",i)
    print("\n")
    
#break
for i in range(1,77):
    print("numero:",i)
    if i==7:
        break
    
#Outra forma de fazer aquele jogo de repetição
while True:
    x=str(input("Digite X se você quiser sair do jogo: "))
    if x.lower() == 'x':
        break
            
#Mensagem de bem-vindo 
print("Bem-vindo(a)! Eu sou seu chatbot (Digite X para sair)")
pergunta = str(input("Qual é a sua pergunta? ")) 

while True:
    print("Aqui será a resposta do bot")
    pergunta = str(input("Possui mais alguma pergunta: ")) 
    if pergunta.lower() == 'x':
        break          
    
print("Muito obrigado por usar meu chatbot!")    