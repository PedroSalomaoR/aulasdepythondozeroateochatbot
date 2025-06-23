#Aula de operadores lógicos
#and
nota1= float(input("Digite a primeira nota: "))
nota2= float(input("Digite a primeira nota: "))
if nota1>5 and nota2>5:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")

#Not
login = input("Você está logado? (s/n): ")

if not login.lower() == "s":
    print("Acesso negado. Faça login.")
else:
    print("Acesso autorizado!")

#or
idade = int(input("Digite sua idade: "))
temautorizacao= input("Tem a autorização dos pais(s/n): ")

if idade>=18 or temautorizacao.lower=='s':
    print("Acesso autorizado!")
else:
    print("Acesso Negado!")