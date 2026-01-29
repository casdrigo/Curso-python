"""
Atividade 9. Verificando a paridade de um número

Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar.
Essa verificação será usada para definir ações diferentes dentro do jogo.
Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.
"""

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'o valor {numero} é par. ')
else:
    print(f'o valor {numero} é impar.')