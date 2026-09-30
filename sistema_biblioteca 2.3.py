from datetime import date


# ==============================
# CLASSE LIVRO
# ==============================

class Livro:

    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def exibir_dados(self):
        print("Código:", self.codigo)
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Ano:", self.ano)

        if self.disponivel:
            print("Status: Disponível")
        else:
            print("Status: Emprestado")

    def emprestar(self):

        # Verifica se o livro está disponível
        if self.disponivel:

            self.disponivel = False

            print("Empréstimo realizado!")

        else:

            print("Livro indisponível!")
            print("Este livro já foi emprestado.")

    def devolver(self):

        # Verifica se o livro foi emprestado
        if not self.disponivel:

            self.disponivel = True

            print("Devolução realizada!")

        else:

            print("O livro não está emprestado.")


# ==============================
# LISTA DA BIBLIOTECA
# ==============================

biblioteca = []


# ==============================
# FUNÇÕES DO SISTEMA
# ==============================

def exibir_menu():

    print("\n===============")
    print(" 1 - Cadastrar")
    print(" 2 - Listar")
    print(" 3 - Pesquisar")
    print(" 4 - Alterar")
    print(" 5 - Excluir")
    print(" 6 - Quantidade")
    print(" 7 - Emprestar")
    print(" 8 - Devolver")
    print(" 9 - Sair")
    print("===============")


def cadastrar_livro(biblioteca):

    while True:

        print("\n===== CADASTRO DE LIVRO =====")

        livro_codigo = input("Qual o código do livro: ")

        if livro_codigo == "":
            print("\nErro! Não pode deixar vazio...")
            continue

        livro_titulo = input("Qual o título do livro: ")

        if livro_titulo == "":
            print("\nErro! Não pode deixar vazio...")
            continue

        livro_autor = input("Qual o nome do autor do livro: ")

        if livro_autor == "":
            print("\nErro! Não pode deixar vazio...")
            continue

        livro_ano = input("Qual o ano de publicação: ")

        if livro_ano == "":
            print("\nErro! Não pode deixar vazio...")
            continue

        livro_ano = int(livro_ano)

        livro = Livro(
            livro_codigo,
            livro_titulo,
            livro_autor,
            livro_ano
        )

        biblioteca.append(livro)

        print("\nLivro cadastrado com sucesso!")

        continuar = input(
            "\nDeseja cadastrar outro livro? (s/n): "
        )

        if continuar.lower() == "n":
            break


def listar_livros(biblioteca):

    if len(biblioteca) == 0:

        print("\nNenhum livro cadastrado.")
        return

    print("\n===== LIVROS CADASTRADOS =====")

    for livro in biblioteca:

        livro.exibir_dados()

        print("------------------")


def buscar_livro(biblioteca, codigo):

    for livro in biblioteca:

        if livro.codigo == codigo:
            return livro

    return None


def exibir_livro(livro):

    livro.exibir_dados()


def pesquisar_livro(biblioteca):

    codigo_busca = input(
        "\nDigite o código do livro que deseja: "
    )

    if codigo_busca == "":
        print("Erro! Não pode deixar vazio...")
        return

    livro_encontrado = buscar_livro(
        biblioteca,
        codigo_busca
    )

    if livro_encontrado is not None:

        print("\nLivro encontrado!")

        exibir_livro(livro_encontrado)

    else:

        print("Livro não encontrado!")


def alterar_livro(biblioteca):

    codigo_busca = input(
        "\nCódigo do livro que deseja alterar: "
    )

    if codigo_busca == "":
        print("Erro! Não se pode deixar vazio...")
        return

    livro = buscar_livro(
        biblioteca,
        codigo_busca
    )

    if livro is None:

        print("Livro não encontrado!")
        return

    novo_titulo = input("Novo título: ")
    novo_autor = input("Novo autor: ")
    novo_ano = int(input("Novo ano: "))

    livro.titulo = novo_titulo
    livro.autor = novo_autor
    livro.ano = novo_ano

    print("Livro atualizado!")


def excluir_livro(biblioteca):

    codigo_busca = input(
        "\nCódigo do livro que deseja excluir: "
    )

    if codigo_busca == "":
        print("Erro! Não se pode deixar vazio...")
        return

    livro = buscar_livro(
        biblioteca,
        codigo_busca
    )

    if livro is None:

        print("Livro não encontrado!")
        return

    biblioteca.remove(livro)

    print("Livro excluído!")


def emprestar_livro(biblioteca):

    codigo_busca = input(
        "\nCódigo do livro para empréstimo: "
    )

    if codigo_busca == "":
        print("Erro! Não se pode deixar vazio...")
        return

    livro = buscar_livro(
        biblioteca,
        codigo_busca
    )

    if livro is None:

        print("Livro não encontrado!")
        return

    # Verifica se o livro está disponível
    if livro.disponivel:

        livro.emprestar()

    else:

        print("\nLivro indisponível!")
        print("Este livro já foi emprestado.")


def devolver_livro(biblioteca):

    codigo_busca = input(
        "\nCódigo do livro para devolução: "
    )

    if codigo_busca == "":
        print("Erro! Não se pode deixar vazio...")
        return

    livro = buscar_livro(
        biblioteca,
        codigo_busca
    )

    if livro is None:

        print("Livro não encontrado!")
        return

    # Verifica se o livro foi emprestado
    if not livro.disponivel:

        livro.devolver()

    else:

        print("\nO livro não está emprestado.")


def quantidade_livros(biblioteca):

    quantidade = len(biblioteca)

    return quantidade


def registrar_data():

    hoje = date.today()

    return hoje


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

while True:

    exibir_menu()

    try:

        opcao = int(
            input("\nQual a opção que deseja realizar: ")
        )

    except ValueError:

        print("Erro! Digite apenas números.")

        continue

    if opcao == 1:

        cadastrar_livro(biblioteca)

    elif opcao == 2:

        listar_livros(biblioteca)

    elif opcao == 3:

        pesquisar_livro(biblioteca)

    elif opcao == 4:

        alterar_livro(biblioteca)

    elif opcao == 5:

        excluir_livro(biblioteca)

    elif opcao == 6:

        quantidade = quantidade_livros(biblioteca)

        print(
            "\nQuantidade de livros cadastrados:",
            quantidade
        )

    elif opcao == 7:

        emprestar_livro(biblioteca)

    elif opcao == 8:

        devolver_livro(biblioteca)

    elif opcao == 9:

        print("\nEncerrando Sistema...")

        break

    else:

        print("Erro! Opção inválida...")