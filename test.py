lista = [1.5, 2, 9.7, 7.9, 5, 6]
lista_final = []
total = media = cont = 0

for itens in lista:
    total = itens + total
    cont += 1
    if itens >= 7:
        lista_final.append(itens)
media = total / cont

print(f'acima da média: {lista_final}')
print(f'Média da turma: {media}')
