#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais 
# baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a 
# cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de 
# dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa
# também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais 
# gordo e do mais magro, além da média das alturas e dos pesos dos clientes

lista = []
lista1 = []

while True:
    codigo = int(input("Digite seu código: "))
    if codigo == 0:
        break
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    lista.append(codigo)
    lista.append(altura)
    lista.append(peso)
    lista1.append(lista[:])
    lista.clear()

maior = lista1[0][1]
menor = lista1[0][1]
gordo = lista1[0][2]
magro = lista1[0][2]

for c, v in enumerate(lista1):
    if v[1] > maior:
        maior = v[1]
    if v[1] < menor:
        menor = v[1]
    if v[2] < magro:
        magro = v[2]
    if v[2] > gordo:
        gordo = v[2]

print(maior)
print(menor)
print(gordo)
print(magro)
