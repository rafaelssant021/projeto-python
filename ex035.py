times = ('Corinthians', 'Palmeiras', 'Gremio',
         'Flamengo', 'Vasco', 'Atletico PR', 'Remo',
         'São Paulo', 'Fluminense', 'Mirassol', 'RB Bragantino',
         'Bahia', 'Botafogo', 'Chapecoense', 'Vitoria', 'Internacional',
         'Santos', 'Cruzeiro', 'Coritiba', 'Atletico MG')
print('-='*15)
print(f'Lista de times do brasileirão: {times}')
print('-='*15)
print(f'os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'os 4 ultimos são: {times[-4:]}')
print('-='*15)
print(f'times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'o Fluminese esta na: {times.index("Fluminense")+1}° posição')
