num1 = int(input("Diga um valor: "))
num2 = int(input("Diga outro valor: "))

if num1 == num2:
    num2 = int(input("Devem ser valores diferentes, digite novamente: "))
elif num1 > num2:
    print(num2, num1)
elif num1 < num2:
    print(num1, num2)