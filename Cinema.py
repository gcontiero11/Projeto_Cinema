import Filmes
import Salas
import Sessoes

def menu():
    print("Filmes.....[1]")
    print("Salas......[2]")
    print("Sessões....[3]")
    print("Sair.......[0]")
    opcao = input("-------------> ")
    return opcao

def main():
    print("-=-=-=-=-=-=-")
    print("CINEMA")
    print("-=-=-=-=-=-=-")
    print()
    opcao = -1
    while opcao != '0':
        opcao = menu()
        if opcao == '1':
            Filmes.execFilmes()
        elif opcao == '2':
            Salas.execSalas()
main()