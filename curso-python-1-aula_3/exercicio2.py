def pular_linha ():
    print('\n')

def checar_chave_informacoes_pessoas():
    x = input(f'Digite a chave que quer checar: ')
    if x in informacoes_pessoas:
        print(f'A chave {x} está no dicionario e seu valor é {informacoes_pessoas[x]}!')
    else:
        print(f'A chave {x} não está cadastrada no dicionario!')

informacoes_pessoas = {'nome':'Rodrigo','idade':'23','cidade':'Curitiba'}

print(informacoes_pessoas)


informacoes_pessoas['idade'] = 22

print(informacoes_pessoas)


informacoes_pessoas['profissao'] = 'Estudante'

print(informacoes_pessoas)



del informacoes_pessoas['profissao']

print(informacoes_pessoas)




pular_linha()
'''
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)
'''
quadrado_numero = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }

print(quadrado_numero)

checar_chave_informacoes_pessoas()