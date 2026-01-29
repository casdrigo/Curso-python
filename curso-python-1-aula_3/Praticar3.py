"""
Atividade 3. Temperatura dos servidores

Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C.
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

"""

temperatura = int(input('Digite a temperatura atual: '))

if temperatura > 25:
    print(f'ALERTA! Temperatura em {temperatura}°C, Acima do limite permitido!')

else:
    print(f'Temperatura em {temperatura}°C, tudo tranquilo! ')