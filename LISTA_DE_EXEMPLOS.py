from random import randint
numero = randint(25, 25)
from time import sleep
sleep(1)
from datetime import date
ano = date.today().year
import math
raiz = math.sqrt(numero)
#raiz = numero ** 0.5 tambem da certo
print(raiz)
#if e % 3 == 0: Pega apenas os divisiveis por 3...
from operator import itemgetter
jogo = {'jogador1': 1,
        'jogador2': 5}
ranking = {}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#\/ \/
#faz um sorted pegando apenas os numeros com itemgetter(1) e ordena todo...
# o conjunto apartir dele, e o reverse faz ficar do maior para menor

#-----------------------------F A T I A M E N T O--------------------------------
from random import shuffle, choice, sample
mylist = ('Pedro', 'Jose', 'Maria', 'Joana')
r = choice(mylist)#Escolhe 1 nome da lista aleatório
res = sample(mylist, len(mylist))#embaralha a lista  mostra toda a lista embaralhada
frase = str('a casa é feia').upper()
print ('A letra A aparece {} vezes na frase'.format(frase.upper().count('A')))
print ('Aparece a primeira vez na posição {}'.format(frase.strip().find('A')))
print ('A ultima vez que aparece é na posição {}'.format(frase.strip().rfind('A')))
nomea = str('Romulo A G Rueda').split()#Quebra a frase em blocos
print ('Seu primeiro nome é {}.'.format(nomea[0]))
print ('Seu sobrenome é {}.'.format(nomea[len(nomea)-1]))
frase_nova = ''.join(frase)
novo_texto = frase_nova [::-1] #recebe a frase da posição 0 a ultima de tras para frente

print(f'o numero {numero:.2f}')#2 casas decimais
#\n quebra a linha ----- , end=' ' NÂO quebra a linha

#conversao seg, min, horas
segundos = 3699
minutos = int(segundos / 60)
resto_segundos = segundos % 60
print(f'{segundos}s é igual a {minutos}m e {resto_segundos}s')
horas = int((segundos / 60) / 60)
minutos = int(minutos % 60)
print(f'{segundos}s são igual a {horas}h, {minutos}m e {resto_segundos}s')
