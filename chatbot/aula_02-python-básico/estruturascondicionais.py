#Aula de estruturas condicionais

#if
idade = int(input("Qual é a sua idade: "))
if idade >= 18:
    print("Você é maior de idade!")
    
#else
idade2 = int(input("Qual é a sua idade: "))
if idade2 >=18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
    
#elif
temperatura = int(input("Qual é a temperatura atual(graus celsius)? "))

if temperatura >=30:
    print("Hoje está muito quente, vá tomar um sorvete de morango.")
elif temperatura >= 20 and temperatura<=29:    
    print("Hoje o dia está agradável para sair.")
else:
    print("Hoje o dia está muito frio, tome cuidado para não ficar resfriado!")