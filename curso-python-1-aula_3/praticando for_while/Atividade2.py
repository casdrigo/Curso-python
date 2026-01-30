# André está testando um novo recurso no backend do Buscante que processa dados em um loop.
# Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
# Qual é o problema do código de André e como resolver? Compartilhe com a gente no fórum!

# contador = 0
#
# while contador < 10:
#     print("Processando dados...")

contador = 0

while contador < 10:
    print("Processando dados...")

    contador += 1                       # Atualiza o contador para evitar o loop infinito