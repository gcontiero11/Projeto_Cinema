import os

class Salas:
    deletado = 0
    numero = -1
    capacidade = -1 #100 ou 200

def retornaNumeroValido(msgInput):
    EhNumero = False
    while not EhNumero:
        numero = input(msgInput)
        if not numero.isnumeric():
            print("\nNúmero Inválido!")
            print("Favor digitar um número inteiro \n")
        else:
            EhNumero = True
    return int(numero)

def isNumber(numero):
    if(str(numero).isnumeric()):
        return True
    else:
        return False
def abrirArquivo(nomeArquivo):
    salas = []
    if not os.path.exists(nomeArquivo):
        return salas
    arq = open(f"{nomeArquivo}" , 'r')
    for linha in arq:
        infos = linha.split(';')
        sala = Salas()
        sala.deletado = int(infos[0])
        sala.numero = int(infos[1])
        sala.capacidade = int(infos[2])

        salas.append(sala)
    arq.close()
    return salas

def sobrescreverArquivo(nomeArquivo , salas):
    arq = open(f"{nomeArquivo}",'w')
    for sala in salas:
        arq.write(str(sala.deletado) + ';' + str(sala.numero) + ';' + str(sala.capacidade) + "\n")
    arq.close

def leNumeroDaSala(salas):
    numeroDeSalaInvalido = True
    while numeroDeSalaInvalido:
        numeroDeSalaInvalido = False
        numero = int(retornaNumeroValido("Digite o Número da sala:"))
        for elem in salas:
            if numero == elem.numero and elem.deletado == 0:
                numeroDeSalaInvalido = True
                print("Já existe uma sala com este número")
                break
    return numero


def inserirSala(salas):
    sala = Salas()
    sala.deletado = 0
    sala.numero = -1
    sala.capacidade = 0
    
    sala.numero = leNumeroDaSala(salas);
    while sala.capacidade != 100 and sala.capacidade != 200:
        sala.capacidade = retornaNumeroValido("Digite a Capacidade (100 ou 200):")
    salas.append(sala)
    return salas

def listarSalas(salas):
    i = 0
    for sala in salas:
        i += 1
        imprimirSala(sala,i)
    print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")

def imprimirSala(sala,i):
    if i > 0:        
        print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
        print(f"Sala [{i}]\n")
        print(f"Número : {sala.numero}")
        print(f"Capacidade sala : {sala.capacidade}")
    else:
        print("-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=-=-=-")
        print("\n")
        print(f"Número : {sala.numero}")
        print(f"Capacidade sala : {sala.capacidade}")
        print("\n")

def acharSala(salas,num):
    i = 0
    for sala in salas:
        if sala.numero == int(num):
            return sala
        i += 1
    return -1

def procurarSala(salas):
    numero = retornaNumeroValido("Digite o Número da sala ou 0 caso queira voltar: ")
    if numero == "0":
        print("Voltando")
        pass
    sala = acharSala(salas,numero)
    while sala == -1:
        print("\nSala não encontrada!")
        print("Verifique se o número da sala existe")
        numero = retornaNumeroValido("Digite o Número da sala ou 0 caso queira voltar: ")
        if numero == "0":
            print("Voltando")
            pass
        sala = acharSala(salas,numero)
    imprimirSala(sala,-1)

def alteraSala(salas):
    numeroSala = retornaNumeroValido("Digite o numero da sala que deseja editar: ")
    sala = acharSala(salas,numeroSala)
    while sala == -1:
        print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=")
        print("Este numero de sala NÃO existe!")
        print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=")
        numeroSala = retornaNumeroValido("Digite o numero da sala que deseja editar: ")
        sala = acharSala(salas,numeroSala)
    opcao = -1
    while opcao != 0:
        opcao = menuAlteraSala()
        if opcao == 1:
            sala.numero = alteraNumeroSala(salas,sala) 
        elif opcao == 2:
            sala.capacidade = alteraCapacidade(salas,sala)
        elif opcao == 0:
            print("Voltando...")
        else:
            print("-=-=-=--=-=-=-=")
            print("Opção inválida!")
            print("-=-=-=--=-=-=-=")
    return salas
 
def menuAlteraSala():
    print("O que deseja mudar?")
    print("Numero.......[1]")
    print("Capacidade...[2]")
    print("Voltar.......[0]")
    opcao = retornaNumeroValido("-------------> ")
    return opcao

def alteraNumeroSala(salas,sala):
    print(f"Numero antigo: {sala.numero}")
    sala.numero = retornaNumeroValido("Numero novo: ")
    sala = acharSala(salas,sala.numero)
    while sala != -1:
        print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
        print("Este numero de sala já existe!")
        print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-")
        sala.numero = retornaNumeroValido("Numero Novo: ")
        sala = acharSala(salas,sala.numero)
    return sala.numero

def alteraCapacidade(sala):
    print(f"Capacidade antiga: {sala.capacidade}")
    sala.capacidade = retornaNumeroValido("Capacidade nova: ")
    return sala.capacidade
def menu():
    print("Escolha uma Opção")
    print("Inserir Sala........[1]")
    print("Listar Salas........[2]")
    print("Procurar uma Sala...[3]")
    print("Alterar uma Sala....[4]")
    print("Remover Sala........[5]")
    print("Sair................[0]")

def main():
    menu()
    opcao = retornaNumeroValido("------------> ")

    nomeArquivo = "salas.txt"

    while opcao != 0:
        salas = abrirArquivo(nomeArquivo)

        #INSERIR
        if opcao == 1:
            print("\n")
            salas = inserirSala(salas)
            sobrescreverArquivo(nomeArquivo,salas)

        #LISTAR
        elif opcao == 2:
            print("\n")
            listarSalas(salas)

        #PROCURAR
        elif opcao == 3:
            print("\n")
            procurarSala(salas)

        #ALTERAR
        elif opcao == 4:
            print("\n")
            salas = alteraSala(salas)
            sobrescreverArquivo(nomeArquivo,salas)

        #REMOVER
        elif opcao == 5:
            print("\n")
            print(opcao)

        #SAIR
        elif opcao == 0:
            print("\n")
            print("SAINDO DO PROGRAMA...")

        #ERRO
        else:
            print("\nOpção Inválida!")
            print("Favor digitar um número dentre as opções\n")

        if opcao != 0:
            print("\n")
            menu()
            opcao = retornaNumeroValido("------------> ")
