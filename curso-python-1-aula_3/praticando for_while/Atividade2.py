# André está testando um novo recurso no backend do Buscante que processa dados em um loop.
# Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
# Qual é o problema do código de André e como resolver? Compartilhe com a gente no fórum!

# contador = 0
#
# while contador < 10:
#     print("Processando dados...")
# Aqui é bem simples, está inifinito pois o contador não sobe, para resolver é só aplicar um contador +1 ao final do loop


contador = 0

while contador < 10:
    print("Processando dados...")
    contador +=1                    #atualiza o valor fazendo não entrar em loop infinito