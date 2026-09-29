opcao=0
lista_livro=[]
while opcao != 3:
    print("\n1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Sair")
    opcao=int(input("\nESCOLHA UMA OPCÃO: \n"))
    if opcao == 1:
        nc=int(input("\nQuantos livros Deseja Cadastrar:"))
        if nc == "":
            print("\nError! Não se pode deixar vazio...")
        else:
            for i in range(1,nc+1):
                livro=input(f"\nNome do livro {i}: ")
                lista_livro.append(livro)

    elif opcao == 2:
        for indice, contagem in enumerate(lista_livro):
            print(indice,"-" ,contagem,)

    elif opcao == 3:
        print("\nSaindo...")
        False

    else:
        print("\nError! Opcão inválida...")