"""
Atividade 7. Média escolar
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media < 5:
    print(f'sua média foi {media}, Reprovado!')
elif 5<= media <7:
    print(f'sua média foi {media}, está de recuperação!')
else:
    print(f'sua média foi {media}, Aprovado!')