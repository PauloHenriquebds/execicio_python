base = float(input("Qual a base do triangulo?: "))

while base <= 0:
    base = float(input("A base tem que ser maior que 0: "))

altura = float(input("Qual a altura do triangulo?: "))

while altura <= 0:
    altura = float(input("A altura tem que ser maior que 0: "))

area = (base * altura)/2

print(f"A area do triangulo é: {area}")