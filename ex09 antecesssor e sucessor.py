while True:
    num = int(input("Diga um numero: "))
    opc = input("Digite 1 para ver o antecessor ou 2 para ver o sucessor ou 3 para encerrar: ")

    if opc == '1':
        sub = num - 1
        print(f"O antecessor a ele é: {sub}")

    elif opc == '2':
        ad = num + 1
        print(f"O sucessor a ele é: {ad}")

    elif opc == '3':
        print("Fim da operação 👍")
        break

    else:
        print("Opção invalida")