import os

class Filme:
    deletado = 0
    titulo = ""
    genero = ""
    duracao = -1
    ano = -1
    codico = -1

def imprime_filme(filme):
    print(f"Título: {filme.titulo}")
    print(f"Gênero: {filme.genero}")
    print(f"Duração: {filme.duracao}")
    print(f"Ano de lançamento: {filme.ano}")
    print(f"Código: {filme.codigo}")

def buscar_filme(lista_filmes,codigo):
    i = 0
    for filme in lista_filmes:
        if codigo == filme.codigo and filme.deletado == 0:
            return filme
        i += 1
    print("Filme não encontrado")
    return -1

def menu():
    print("Inserir filme....[1]")
    print("Listar filmes....[2]")
    print("Procurar filme...[3]")
    print("Remover filme....[4]")
    print("Editar filme.....[5]")
    print("Sair.............[0]")
    opcao = input("----------------> ")
    print()
    return opcao

def menu_editar():
    print("O que deseja editar?")
    print()
    print("Titulo..............[1]")
    print("Gênero..............[2]")
    print("Duração.............[3]")
    print("Ano de lançamento...[4]")
    print("Voltar..............[0]")
    opcao = input("-------------------->")
    return opcao

def Inserindo_filme(lista_filmes):
    filme = Filme()
    filme.deletado = 0
    filme.titulo = input("Digite o título: ")
    filme.genero = input("Digite o genero do filme: ")
    filme.duracao = int(input("Digite a duração do filme: "))
    filme.ano = int(input("Digite o ano de lançamento do filme: "))
    filme.codigo = int(input("Digite o código do filme: "))
    invalidCode = True
    while invalidCode:
        invalidCode = False
        for elem in lista_filmes:
            if filme.codigo == elem.codigo and elem.deletado == 0:
                invalidCode = True
                print("Código inválido!!!")
                print()
                filme.codigo = int(input("Digite outro código para o Filme: "))
                break
    lista_filmes.append(filme)
    print("Filme adicionado com sucesso!")

def listando_filme(lista_filmes):
    lista_vazia = True
    for filme in lista_filmes:
        if(filme.deletado == 0):
            lista_vazia = False
            break
    if lista_vazia:
        print("Não há filmes no catálogo.")
    else:
        numero_filmes = 0
        indice_filme = 0
        print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
        for filme in lista_filmes:
            if filme.deletado == 0:
                numero_filmes += 1
                print(f"Filme [{numero_filmes}]: ")
                imprime_filme(filme)
                print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")

def procurando_filme(lista_filme):
    code = int(input("Digite o código do filme: "))
    i = 0
    print()
    for filme in lista_filme:
        if filme.codigo == code and filme.deletado == 0:
            print("Filme encontrado!!")
            print("-=-=-=-=-=--=-=-=-=-=-=-=-")
            imprime_filme(filme)
            print("-=-=-=-=-=--=-=-=-=-=-=-=-")
            return
    print("Não há nenhum filme com este código.")

def salvar_filmes(filmes):
    arq = open("filmes.txt",'w')
    for filme in filmes:
        arq.write(str(filme.deletado) + ';' + filme.titulo + ';' + filme.genero + ';' + str(filme.duracao) + ';' + str(filme.ano) + ';' + str(filme.codigo) + "\n")
    arq.close

def abrir_arquivo(nome_arquivo):
    filmes = []
    if not os.path.exists("filmes.txt"):
        return filmes
    arq = open(f"{nome_arquivo}" , 'r')
    for linha in arq:
        infos = linha.split(';')
        filme = Filme()
        filme.deletado = int(infos[0])
        filme.titulo = infos[1]
        filme.genero = infos[2]
        filme.duracao = int(infos[3])
        filme.ano = int(infos[4])
        filme.codigo = int(infos[5])
        filmes.append(filme)
    arq.close()
    return filmes

def remover_filme(lista_filmes):
    code = int(input("Insira o código do filme: "))
    for filme in lista_filmes:
        if code == filme.codigo and filme.deletado == 0:
            filme.deletado = 1
            print("Deletado com sucesso!")
            return lista_filmes
    print("O Filme não foi encontrado.")
    return lista_filmes

def editar_filme(lista_filmes):
    code = int(input("Digite o código do filme que deseja editar: "))
    filme = buscar_filme(lista_filmes,code)
    if filme != -1:
        opcao = menu_editar()
        if opcao == '1':
            filme = editar_Titulo_filme(filme)
        elif opcao == '2':
            filme = editar_Genero_filme(filme)
        elif opcao == '3':
            filme = editar_Duracao_filme(filme)
        elif opcao == '4':
            filme = editar_Ano_filme(filme)
        else:
            print("Opção não reconhecida!")
    return lista_filmes

def editar_Titulo_filme(filme):
    print(f"Título atual: {filme.titulo}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    filme.titulo = input("Título novo: ")
    return filme

def editar_Genero_filme(filme):
    print(f"Gênero atual: {filme.genero}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    filme.genero = input("Gênero novo: ")
    return filme

def editar_Duracao_filme(filme):
    print(f"Duração atual: {filme.duracao}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    filme.duracao = input("Duração nova: ")
    return filme

def editar_Ano_filme(filme):
    print(f"Ano de Lançamento atual: {filme.ano}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    filme.ano = input("Ano de Lançamento novo: ")
    return filme

def main():
    filmes = abrir_arquivo("filmes.txt")
    opcao = "-1"
    while opcao != '0':
        opcao = menu()
        if opcao == '1':
            print("Inserindo filme...")
            print()
            Inserindo_filme(filmes)
            salvar_filmes(filmes)
            print()
        elif opcao == '2':
            print("Listando Filme...")
            print()
            listando_filme(filmes)
            print()
        elif opcao == '3':
            print("Procurando filme...")
            print()
            procurando_filme(filmes)
            print()
        elif opcao == '4':
            print("Removendo Filme...")
            filmes = remover_filme(filmes)
            print()
        elif opcao == '5':
            print("Editando filme...")
            print()
            filmes = editar_filme(filmes)
            print()
        elif opcao == '0':
            print("Saindo do Programa...")
            salvar_filmes(filmes)
        else:
            print("Opção invalida!!!")
            print()