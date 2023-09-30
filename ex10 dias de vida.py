idade = int(input("Qual a sua idade?: "))
mes = int(input("Qual o mes que você nasceu?: "))
dia = int(input("Qual o dia?: "))

dia_ano = idade * 365
dia_mes = mes * 30
dias_vida = dia + dia_ano + dia_mes

print(f"Você vive: {dias_vida} dias ")