#Aula sobre listas em python
carrinho = [
    'Maracujá',
    'Arroz',
    'Feijão',
    'Batata',
    'Macarrão',
    'Salada'
]

#pega o primeiro valor da lista
print(carrinho[0])

#add valor no final da lista
carrinho.append('Melão')
print(carrinho)

#remove valor selecionado
carrinho.pop(3)
print(carrinho)

#slicing da lista, vai exibir os dois primeiros itens
print(carrinho[0:2])