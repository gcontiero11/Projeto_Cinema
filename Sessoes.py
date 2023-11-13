class Filme:
    deletado = 0
    titulo = ""
    genero = ""
    duracao = -1
    ano = -1
    codico = -1

class Salas:
    deletado = 0
    numero = -1
    capacidade = -1 #100 ou 200

class Sessoes:
    sala = Salas
    filme = Filme