hora_inicio = int(input('Digite a hora de inicio da partida de xadrez: '))
hora_fim = int(input('Digite a hora do fim da partida de xadrez: '))

if hora_inicio >= hora_fim:
    resultado = hora_fim - (hora_inicio - 24)
else:
    resultado = hora_fim - hora_inicio

print(f'A duração do jogo foi de {resultado}')