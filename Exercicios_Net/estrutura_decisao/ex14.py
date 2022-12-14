"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
conceito = situacao = ""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 9 and media <= 10:
    conceito = "A"
    situacao = "APROVADO"
if media >= 7.5 and media < 9:
    conceito = "B"
    situacao = "APROVADO"
if media >= 6 and media < 7.5:
    conceito = "C"
    situacao = "APROVADO"
if media >= 4 and media < 6:
    conceito = "D"
    situacao = "REPROVADO"
if media < 4 and media >= 0:
    conceito = "E"
    situacao = "REPROVADO"

print(f"Você tirou {nota1:.2f} e {nota2:.2f}, sua média foi {media:.2f}")
print(f"Com essas notas voce teve conceito '{conceito}' e está {situacao}!")
