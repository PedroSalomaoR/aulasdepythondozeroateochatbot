#Aula de operadores de comparação
nome = 'Pedro Salomão'
idade = 19
altura = 1.85

# Operadores de comparação
print(idade == 19)  # Igualdade
print(idade != 20)  # Diferença
print(idade > 18)   # Maior que
print(idade < 20)   # Menor que
print(idade >= 19)  # Maior ou igual a
print(idade <= 19)  # Menor ou igual a

#Teste de alguns operadores
if idade >= 18:
    print(f"Olá {nome}, você tem {idade} anos, é maior de idade");
else:
    print(f"Olá {nome}, você tem {idade} anos, é menor de idade");
    