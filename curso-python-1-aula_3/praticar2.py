"""
Atividade 2. Calculando o tempo total de projeto

Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades:
A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores
inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto.
Se algum valor for negativo, mostre uma mensagem informando o erro.

"""

a = int(input("Informe os dias para a atividade A: "))
b = int(input("Informe os dias para a atividade B: "))
c = int(input("Informe os dias para a atividade C: "))

tempo_total = a + b + c

if a<0 or b<0 or c<0:
    print("Erro: os dias não podem ser negativos!")
else:
    print(f"Vai demorar {tempo_total} dias!")