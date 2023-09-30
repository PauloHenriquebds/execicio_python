maca = int(input("Quantas maçãs você comprou?: "))

if maca > 11:
    total = maca * 1
else:
    total = maca * 1.30

print(f"O total a pagar por {maca} é {total:.2f}")