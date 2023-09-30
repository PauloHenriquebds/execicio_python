repet = int(input("Diga quantas vezes vc quer repetir:  "))
soma = 0
for n in range(repet):
    num = float(input("Diga um numero: "))
    soma += num

media = soma /repet

print(f"A soma dos numeros é: {soma}")
print(f"A media deles é: {media}")