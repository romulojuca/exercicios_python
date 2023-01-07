#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o décimo termo.

lista = []
lista2 = []


for c in range(0, 9):
    if c == 0:
        lista.append(1)
    lista.append(lista[c] + lista[c-1])


print(lista)
