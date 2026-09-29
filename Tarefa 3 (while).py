lista_nome=[]
quant=int(input("Quantos alunos serão cadatrados(número inteiro): "))
contador=1
while contador <= quant:
    nome=input(f"\nDigite o nome do aluno {contador}: ")
    lista_nome.append(nome)
    contador=contador+1
    print("Aluno cadastrado:",nome)
print("\n====== NOME DOS ALUNOS CADASTRADOS: ======")
print("======    Por Ordem De Cadastro     ======")
for indice, contagem in enumerate(lista_nome):
    print(indice,"-" ,contagem,)


