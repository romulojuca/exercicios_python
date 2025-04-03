gols = []
cont = 0
dados = {
        'nome': str(input('nome:')),
        'numero partidas': int(input('n partidas:')),
        }
for e in range(0, dados['numero partidas']):
    gols.append(int(input(f'Quantos gols na {e+1} partida? ')))

dados['gols'] = gols
for i, e in dados.items():
    print(f'O Campo {i} tem o valor {e}.')

print(f'O jogador {dados["nome"]} jogou {dados["numero partidas"]} partidas!')

for i, e in enumerate(dados['gols']):
    print(f'=> Na partida {i} ele fez {e} gols.')
    cont += e
print(f'Total de {cont} gols')
