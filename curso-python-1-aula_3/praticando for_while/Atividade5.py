"""
Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. Ela organizou uma lista com o
nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None:

"""

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for i in projetos:
    if i is None:
        print('Projeto ausente')
    else:
        print(i)