maior = 0
menor1 = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor1 = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor1:
            menor1 = peso

print ('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor1))
