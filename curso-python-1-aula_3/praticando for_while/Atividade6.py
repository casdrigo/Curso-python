"""
José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico
 é encontrado. A lista de livros já cadastrados no sistema é a seguinte:
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

Ajude José a criar um programa que percorra a lista e exiba a mensagem "Livro encontrado: <nome do livro>" assim que o
livro "O Hobbit" for encontrado. Após encontrar o livro, o programa deve parar imediatamente a busca, sem verificar os
livros restantes.
"""

busca = "O Hobbit"

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
print('Buscando o livro: O Hobbit em nosso banco de dados')
for livro in livros:
    if livro == busca:
        print(f'Livro encontrado: {livro}')
        break
