"""
Atividade 5. Controlando o orçamento mensal
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos
e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar
se ele ultrapassou o limite ou ainda está dentro do orçamento.

"""

orcamento = 3000.00

despesas = float(input('Digite o total de despesas do mês (R$): '))

if despesas < orcamento:
    print(f'Se suas despesas são de: {despesas} e teu orçamento maximo é de {orcamento}, ainda te sobra R${orcamento - despesas}.\nTá muito tranquilo!')
else:
    print(f'Se suas despesas são de: {despesas} e teu orçamento maximo é de {orcamento}, Você está devendo R${orcamento - despesas}.\nInfelizmente vai pro serasa!')