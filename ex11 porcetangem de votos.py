voto_branco = int(input("Quantos votos em branco?: "))
voto_nulo = int(input("Quantos votos nulos?: "))
voto_valido = int(input("Quantos votos validos?: "))

eleitor = voto_valido + voto_nulo + voto_branco

branco = (voto_branco / eleitor)*100
nulo = (voto_nulo / eleitor)*100
valido = (voto_valido / eleitor)*100

print(f"A porcentagem de votos brancos é: {branco:.1f} %")
print(f"A porcentagem de votos nulos é: {nulo:.1f} %")
print(f"A porcentagem de votos validos é: {valido:.1f} %")