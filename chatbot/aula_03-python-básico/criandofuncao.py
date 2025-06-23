#Aula sobre a criação de função
def calcular_media(n1, n2, n3):
    media = (n1+n2+n3)/3
    return media
    
nota1=float(input("Qual foi sua primeira nota: "))
nota2=float(input("Qual foi sua segunda nota: "))
nota3=float(input("Qual foi sua terceira nota: "))

resultado = calcular_media(nota1,nota2,nota3)

print(f"A sua média final é de {resultado:.1f}")

#criando outra função
def verificar_paridade(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

num = int(input("Digite um número: ")) 

teste = verificar_paridade(num)

print(f"{num} é {teste}")

#outra função
def verificador_de_voto(idade):
    if idade>=18 and idade<=70:
        return "Voto Obrigatório!"
    elif (idade >= 16 and idade <= 17) or idade > 70:
        return "Voto facultativo!"
    else:
        return "Não pode votar!"
    
idade = int(input("Qual é a sua idade: "))    

teste2 = verificador_de_voto(idade)

print(f"Pessoas Com {idade} anos, {teste2}") 

