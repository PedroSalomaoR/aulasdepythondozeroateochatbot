#Aula sobre a biblioteca random
import random
print(random.randint(1, 10))#imprime um número aleatório entre 1 e 10
print(random.uniform(1, 5))#imprime um número quebrado aleatório entre 1 e 5
print(random.choice(["Python", "Java"]))#imprime um item aleatório da lista
print(random.sample([1, 2, 3, 4], 2))#imprime dois itens aleatórios da lista

#exemplos de aplicações
#numero secreto
numerosecreto=random.randint(1,10)
tentativas = 5
tentativadenumero = int(input("Digite o numero secreto: "))
if numerosecreto>tentativadenumero:
    print(f"O número secreto é maior que {tentativadenumero}")
    tentativas=tentativas-1
if numerosecreto<tentativadenumero:
    print(f"O número secreto é menor que {tentativadenumero}")
    tentativas=tentativas-1
while (numerosecreto != tentativadenumero) or tentativas>0:

    tentativadenumero = int(input("Digite o numero secreto: "))
    if numerosecreto>tentativadenumero:
        print(f"O número secreto é maior que {tentativadenumero}")
        tentativas=tentativas-1
    if numerosecreto<tentativadenumero:
        print(f"O número secreto é menor que {tentativadenumero}")
        tentativas=tentativas-1    
    if tentativas==0:
        print(f"Você perdeu o jogo, o numero secreto era: {numerosecreto}")
        break
    if numerosecreto == tentativadenumero:
        print(f"Você ganhou, o numero secreto era: {numerosecreto}")
        break
        
           

#cartas embaralhadas
cartas = ["A", "K", "Q", "J", "10"]
random.shuffle(cartas)
print("Cartas embaralhadas:", cartas)
