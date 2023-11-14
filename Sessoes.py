import os
import Filmes
import Salas

class Filme:
    deletado = 0
    titulo = ""
    genero = ""
    duracao = -1
    ano = -1
    codigo = -1

class Sala:
    deletado = 0
    numero = -1
    capacidade = -1 #100 ou 200

class Sessao:
    deletada = 0
    codigo = -1
    sala = Sala()
    filme = Filme()

def abrirArquivoSessoes(nomeArquivo):
    sessoes = []
    if not os.path.exists(nomeArquivo):
        return sessoes
    arq = open(f"{nomeArquivo}" , 'r')
    for linha in arq:
        infos = linha.split(';')
        sessao = Sessao()
        sessao.deletada = int(infos[0])
        sessao.codigo = int(infos[1])
        sessao.sala = infos[2]
        sessao.filme = infos[3]

        sessoes.append(sessao)
    arq.close()
    return sessoes

def abrirArquivoFilmes(nomeArquivo):
    filmes = []
    if not os.path.exists("filmes.txt"):
        return filmes
    arq = open(f"{nomeArquivo}" , 'r')
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

def abrirArquivoSalas(nomeArquivo):
    salas = []
    if not os.path.exists(nomeArquivo):
        return salas
    arq = open(f"{nomeArquivo}" , 'r')
    for linha in arq:
        infos = linha.split(';')
        sala = Sala()
        sala.deletado = int(infos[0])
        sala.numero = int(infos[1])
        sala.capacidade = int(infos[2])

        salas.append(sala)
    arq.close()
    return salas

def sobrescreverArquivoSESSOES(sessoes):
    arq = open(f"sessoes.txt",'w')
    for sessao in sessoes:
        arq.write(str(sessao.deletada) + ';' + str(sessao.codigo) +  ';' + str(sessao.sala) + ';' + str(sessao.filme) + "\n")
    arq.close

def sobrescreverArquivoFILMES(filmes):
    arq = open("filmes.txt",'w')
    for filme in filmes:
        arq.write(str(filme.deletado) + ';' + filme.titulo + ';' + filme.genero + ';' + str(filme.duracao) + ';' + str(filme.ano) + ';' + str(filme.codigo) + "\n")
    arq.close

def sobrescreverArquivoSALAS(salas):
    arq = open(f"salas.txt",'w')
    for sala in salas:
        arq.write(str(sala.deletado) + ';' + str(sala.numero) + ';' + str(sala.capacidade) + "\n")
    arq.close

def retornaNumeroValido(msgInput):
    EhNumero = False
    while not EhNumero:
        numero = input(msgInput)
        if not numero.isnumeric():
            print("\nNúmero Inválido!")
            print("Favor digitar um número inteiro positivo \n")
        else:
            EhNumero = True
    return int(numero)

def solicitaFilme(filmes):
    Filmes.listando_filme(filmes)
    codigoFilme = retornaNumeroValido("Digite o código do filme que deseja adicionar à sessão: ")
    return Filmes.buscar_filme(filmes,codigoFilme)

def solicitaSala(salas):
    Salas.listarSalas(salas)
    numeroSala = retornaNumeroValido("Digite o numero da sala que deseja adicionar à sessão")
    return Salas.acharSala(salas,numeroSala)

def criaSessao(sessoes,filmes,salas):
    sessao = Sessao()

    sessao.codigo = retornaNumeroValido("Digite o código da sessao: ")
    sessoes
    sessao.deletado = 0

    sessao.filme = solicitaFilme(filmes)
    while sessao.filme == -1:
        sessao.filme = solicitaFilme(filmes)

    sessao.sala = solicitaSala(salas)
    while sessao.sala == -1:
        sessao.sala = solicitaSala(salas)
    sessoes.append(sessao)
    return sessoes    

def imprimeSessao(sessao):
    print(f"Numero Sala: {sessao.sala.numero} ")
    print(f"Titulo Filme: {sessao.filme.titulo} ")

def listarSessoes(sessoes):
    i = 0
    for sessao in sessoes:
        print(f"Sessão [{i+1}]\n")
        imprimeSessao(sessao)
        i += 1


def menuSessoes():
    print("Criar uma sessão....[1]")
    print("Listar sessões......[2]")
    print("Procurar sessao.....[3]")
    print("Remover sessão......[4]")
    print("Sair................[0]")

def execSessoes():
    menuSessoes()
    option = retornaNumeroValido("---------> ")

    while option != 0:
        nomeArquivo = "sessoes.txt"
        sessoes = abrirArquivoSessoes(nomeArquivo)
        nomeArquivo = "filmes.txt"
        filmes = abrirArquivoFilmes(nomeArquivo)
        nomeArquivo = "salas.txt"
        salas = abrirArquivoSalas(nomeArquivo)

        if option == 1:
            sessoes = criaSessao(sessoes,filmes,salas)
            sobrescreverArquivoSESSOES(sessoes)
        if option == 2:
           listarSessoes(sessoes) 
        if option == 3:
            print(option)
        if option == 4:
            print(option)
        if option == 0:
            print("Voltando...")
        else:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("Digite um numero que está no menu!!")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        if option != 0:
            menuSessoes()
            option = retornaNumeroValido("---------> ")