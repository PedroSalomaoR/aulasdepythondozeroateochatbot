#Formatação de String
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual é a sua altura? "))

# Exemplo de formatação de string
print(f"Olá {nome}! Seja bem-vindo(a)! Você tem {idade} anos, sua altura é {altura:.2f} metros")
pergunta = input(f"Bom {nome}, qual é a sua dúvida? ")
print(f"Essa é a sua dúvida: {pergunta}.")