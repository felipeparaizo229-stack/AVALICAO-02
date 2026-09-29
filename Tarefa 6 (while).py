senha=0
while senha != 123:
    senha=int(input(f"\nDigite a senha:"))
    if senha != 123:
        print("Senha Inválida!")
    elif senha == 123:
        print("Acesso permitido!")
        break