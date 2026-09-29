idade=int(input("Digite a idade: "))
while True:
    print("Valor é inválido! Coloque outra idade...")
    idade2=int(input(f"Digite a idade: "))
    if 1 <= idade2 <= 120:
        print("Idade Válida! ")
        break
        