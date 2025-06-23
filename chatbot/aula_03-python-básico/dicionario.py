#Aula sobre dicionário
pessoas = {
    'Maria' : '30',
    'Ana Julia' : '19',
    'Pedro' : '19',
    'Murilo' : '19',
    'Guilherme' : '20'
}

#coletando dados de uma pessoa especifica
print(pessoas['Guilherme'])

#add uma pessoa
pessoas['Adriano'] = 32
print(pessoas)

#removendo pessoas do dicionário
del pessoas['Adriano']
print(pessoas)