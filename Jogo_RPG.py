import os


class Jogo():

    def __init__(self, nome):
        self.nome = nome

    def infopersongem(Self, qual):
        print("ESSE É SEU PERSONAGEM {:s}\n TIPO: {:s}\n ESPÉCIE: {:s}\n VIDA: {:d}\n FORÇA: {:d}".format(
            qual.nome, qual.Tipo, qual.Especie, qual.Vida, qual.Força))

    def atacar(Self, atack, alvo):

        if alvo.Vida > 0:
            alvo.Vida = alvo.Vida - atack.Força
            return alvo.Vida
        else:
            return alvo.Vida

    def defender(Self, alvo, atack):

        if alvo.Vida > 0:
            alvo.Vida = alvo.Vida + (atack.Força - 5)
            return alvo.Vida
        else:
            return alvo.Vida

    def itemcura(Self, player):

        if (hasattr(player, 'Simpatia')):
            player.Vida = player.Vida + player.Simpatia
            return player.Vida

        elif (hasattr(player, 'Honestidade')):
            player.Vida = player.Vida + player.Honestidade
            return player.Vida

        else:
            return player.Vida

    def itemforça(Self, player):

        if (hasattr(player, 'Braveza')):
            player.Força = player.Força + player.Braveza
            return player.Força

        elif (hasattr(player, 'Inteligencia')):
            player.Força = player.Força + player.Inteligencia
            return player.Força

        elif (hasattr(player, 'Magia')):
            player.Força = player.Força + player.Magia
            return player.Força

        else:
            return player.Força

    def conversar(Self, player2, mensagem):
        rspt = mensagem

        while True:
            print("{:s} disse: {:s}".format(Self.nome, rspt))
            rsptpessoa = player2.responder(rspt)
            print("{:s} disse: {:s}".format(player2.nome, rsptpessoa))
            if (rspt == "Não sei dizer") or (rsptpessoa == "Não sei dizer"):
                break
            rspt = input("-->")


class Zumbi(Jogo):
    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Zumbi"
        self.Especie = "Monstro"
        self.Vida = 100
        self.Força = 5
        self.Simpatia = 50


class Dragao(Jogo):

    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Dragão"
        self.Especie = "Monstro"
        self.Vida = 150
        self.Força = 15
        self.Simpatia = 50


class Aldeao(Jogo):

    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Aldeão"
        self.Especie = "Humano"
        self.Vida = 100
        self.Força = 10
        self.Honestidade = 20

    def falar(Self):
        Self.fala = input("->")

    def responder(Self, mensagem):
        if mensagem == "Olá!":
            return "Tudo bem?"
        elif mensagem == "Tudo bem?":
            return "Sim, e você?"
        elif mensagem == "Sim, e você?":
            return "Estou ótimo!"
        elif mensagem == "Até logo!":
            return "Até!"
        elif mensagem == "Tchau!":
            return "Até!"
        else:
            return "Não sei dizer"


class Cavaleiro(Jogo):

    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Cavaleiro"
        self.Especie = "Humano"
        self.Vida = 120
        self.Força = 25
        self.Braveza = 20

    def falar():
        fala = input("->")

    def responder():
        print("Olá, sou um Cavaleiro!")

    def responder(Self, mensagem):
        if mensagem == "Olá!":
            return "Tudo bem?"
        elif mensagem == "Tudo bem?":
            return "Sim, e você?"
        elif mensagem == "Sim, e você?":
            return "Estou ótimo!"
        elif mensagem == "Até logo!":
            return "Até!"
        elif mensagem == "Tchau!":
            return "Até!"
        else:
            return "Não sei dizer"


class Princesa(Jogo):

    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Princesa"
        self.Especie = "Humano"
        self.Vida = 100
        self.Força = 18
        self.Inteligencia = 12

    def responder(Self, mensagem):
        if mensagem == "Olá!":
            return "Tudo bem?"
        elif mensagem == "Tudo bem?":
            return "Sim, e você?"
        elif mensagem == "Sim, e você?":
            return "Estou ótimo!"
        elif mensagem == "Até logo!":
            return "Até!"
        elif mensagem == "Tchau!":
            return "Até!"
        else:
            return "Não sei dizer"


class Mago(Jogo):

    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Mago"
        self.Especie = "Humano"
        self.Vida = 110
        self.Força = 30
        self.Magia = 10

    def falar():
        fala = input("->")

    def responder(Self, mensagem):
        if mensagem == "Olá!":
            return "Tudo bem?"
        elif mensagem == "Tudo bem?":
            return "Sim, e você?"
        elif mensagem == "Sim, e você?":
            return "Estou ótimo!"
        elif mensagem == "Até logo!":
            return "Até!"
        elif mensagem == "Tchau!":
            return "Até!"
        else:
            return "Não sei dizer"


class Bruxa(Jogo):

    def __init__(self, nome):
        Jogo.__init__(self, nome)
        self.Tipo = "Bruxa"
        self.Especie = "Humano"
        self.Vida = 120
        self.Força = 30
        self.Magia = 10

    def falar():
        fala = input("->")

    def responder(Self, mensagem):
        if mensagem == "Olá!":
            return "Tudo bem?"
        elif mensagem == "Tudo bem?":
            return "Sim, e você?"
        elif mensagem == "Sim, e você?":
            return "Estou ótimo!"
        elif mensagem == "Até logo!":
            return "Até!"
        elif mensagem == "Tchau!":
            return "Até!"
        else:
            return "Não sei dizer"


# Corpo do codigo
Nome = input("DIGITE O NOME DO PLAYER 1:")
Escolha = int(input("\n---ESCOLHA SEU PERSONAGEM---\n 1 - ZUMBI\n 2 - DRAGÃO\n 3 - ALDEÃO\n 4 - CAVALEIRO\n 5 - PRINCESA\n 6 - MAGO\n 7 - BRUXA\n DIGITE O NUMERO -->"))

if Escolha == 1:
    Player1 = Zumbi(Nome)
    os.system("cls")

elif Escolha == 2:
    Player1 = Dragao(Nome)
    os.system("cls")

elif Escolha == 3:
    Player1 = Aldeao(Nome)
    os.system("cls")

elif Escolha == 4:
    Player1 = Cavaleiro(Nome)
    os.system("cls")

elif Escolha == 5:
    Player1 = Princesa(Nome)
    os.system("cls")

elif Escolha == 6:
    Player1 = Mago(Nome)
    os.system("cls")

elif Escolha == 7:
    Player1 = Bruxa(Nome)
    os.system("cls")


Nome2 = input("DIGITE O NOME DO PLAYER 2:")
Escolha2 = int(input("\n---ESCOLHA SEU PERSONAGEM---\n 1 - ZUMBI\n 2 - DRAGÃO\n 3 - ALDEÃO\n 4 - CAVALEIRO\n 5 - PRINCESA\n 6 - MAGO\n 7 - BRUXA\n DIGITE O NUMERO -->"))
if Escolha2 == 1:
    Player2 = Zumbi(Nome2)
    os.system("cls")

elif Escolha2 == 2:
    Player2 = Dragao(Nome2)
    os.system("cls")

elif Escolha2 == 3:
    Player2 = Aldeao(Nome2)
    os.system("cls")

elif Escolha2 == 4:
    Player2 = Cavaleiro(Nome2)
    os.system("cls")

elif Escolha2 == 5:
    Player2 = Princesa(Nome2)
    os.system("cls")

elif Escolha2 == 6:
    Player2 = Mago(Nome2)
    os.system("cls")

elif Escolha2 == 7:
    Player2 = Bruxa(Nome2)
    os.system("cls")

comand = Jogo(Nome)

while True:
    decisao = int(input(
        "---OQUE VC DESEJA FAZER---\n 1 - INFO DOS SEUS PERSONAGENS\n 2 - COMBATE\n 3 - CONVERSAR COM PERSONAGEM\n 4 - SAIR DO JOGO\n DIGITE O NUMERO -->"))
    os.system("cls")

    if decisao == 1:
        print("")
        comand.infopersongem(Player1)
        print("")
        print("")
        comand.infopersongem(Player2)
        print("")

    elif decisao == 2:

        while True:
            if (Player1.Vida > 0) and (Player2.Vida > 0):

                combat1 = int(input(
                    "---MENU DE COMBATE PLAYER-1---\n 1 - ATACAR\n 2 - DEFENDER\n 3 - USAR ITEM\n DIGITE O NUMERO -->"))
                os.system("cls")

                combat2 = int(input(
                    "---MENU DE COMBATE PLAYER-2---\n 1 - ATACAR\n 2 - DEFENDER\n 3 - USAR ITEM\n DIGITE O NUMERO -->"))
                os.system("cls")

                if (combat1 == 1) and (combat2 == 2):
                    Player2.Vida = comand.atacar(Player1, Player2)
                    Player2.Vida = comand.defender(Player2, Player1)
                    Player1.Força = Player1.Força - 10

                elif (combat1 == 1) and (combat2 == 1):
                    Player2.Vida = comand.atacar(Player1, Player2)
                    Player1.Vida = comand.atacar(Player2, Player1)

                elif (combat1 == 2) and (combat2 == 1):
                    Player1.Vida = comand.atacar(Player2, Player1)
                    Player1.Vida = comand.defender(Player1, Player2)
                    Player2.Força = Player2.Força - 10

                elif (combat1 == 3) or (combat2 == 3):

                    if (combat1 == 3) and (combat2 != 3):
                        if (hasattr(Player1, 'Simpatia')) or (hasattr(Player1, 'Honestidade')):
                            if (combat1 == 3) and (combat2 == 1):
                                Player1.Vida = comand.itemcura(Player1)
                                Player1.Vida = comand.atacar(Player2, Player1)

                            elif (combat1 == 3) and (combat2 == 2):
                                Player1.Vida = comand.itemcura(Player1)
                                Player2.Vida = comand.defender(
                                    Player2, Player1)
                                Player1.Força = Player1.Força - 10

                        elif (hasattr(Player1, 'Braveza')) or (hasattr(Player1, 'Inteligencia')) or (hasattr(Player1, 'Magia')):
                            if (combat1 == 3) and (combat2 == 1):
                                Player1.Força = comand.itemforça(Player1)
                                Player1.Vida = comand.atacar(Player2, Player1)

                            elif (combat1 == 3) and (combat2 == 2):
                                Player1.Força = comand.itemforça(Player1)
                                Player2.Vida = comand.defender(
                                    Player2, Player1)
                                Player1.Força = Player1.Força - 10

                    elif (combat2 == 3) and (combat1 != 3):
                        if (hasattr(Player2, 'Simpatia')) or (hasattr(Player2, 'Honestidade')):
                            if (combat1 == 1) and (combat2 == 3):
                                Player1.Vida = comand.itemcura(Player1)
                                Player2.Vida = comand.atacar(Player1, Player2)

                            elif (combat1 == 2) and (combat2 == 3):
                                Player2.Vida = comand.usaritem(Player2)
                                Player1.Vida = comand.defender(
                                    Player1, Player2)
                                Player2.Força = Player2.Força - 10

                        elif (hasattr(Player2, 'Braveza')) or (hasattr(Player2, 'Inteligencia')) or (hasattr(Player2, 'Magia')):
                            if (combat1 == 1) and (combat2 == 3):
                                Player2.Força = comand.itemforça(Player2)
                                Player2.Vida = comand.atacar(Player1, Player2)

                            elif (combat1 == 2) and (combat2 == 3):
                                Player2.Força = comand.itemforça(Player2)
                                Player2.Vida = comand.defender(
                                    Player2, Player1)
                                Player2.Força = Player2.Força - 10

                    elif (combat1 == 3) and (combat2 == 3):

                        if ((hasattr(Player1, 'Simpatia')) or (hasattr(Player1, 'Honestidade'))) and ((hasattr(Player2, 'Simpatia')) or (hasattr(Player2, 'Honestidade'))):
                            Player1.Vida = comand.itemcura(Player1)
                            Player2.Vida = comand.itemcura(Player2)

                        elif ((hasattr(Player1, 'Braveza')) or (hasattr(Player1, 'Inteligencia')) or (hasattr(Player1, 'Magia'))) and ((hasattr(Player2, 'Braveza')) or (hasattr(Player2, 'Inteligencia')) or (hasattr(Player2, 'Magia'))):
                            Player2.Força = comand.itemforça(Player2)
                            Player1.Força = comand.itemforça(Player1)

                        elif ((hasattr(Player1, 'Simpatia')) or (hasattr(Player1, 'Honestidade'))) and ((hasattr(Player2, 'Braveza')) or (hasattr(Player2, 'Inteligencia')) or (hasattr(Player2, 'Magia'))):
                            Player1.Vida = comand.itemcura(Player1)
                            Player2.Força = comand.itemforça(Player2)

                        elif ((hasattr(Player2, 'Simpatia')) or (hasattr(Player2, 'Honestidade'))) and ((hasattr(Player1, 'Braveza')) or (hasattr(Player1, 'Inteligencia')) or (hasattr(Player1, 'Magia'))):
                            Player2.Vida = comand.itemcura(Player2)
                            Player1.Força = comand.itemforça(Player1)

            elif (Player1.Vida <= 0) and (Player1.Vida < Player2.Vida):
                print("\n==============================\n")
                print("{:s} VENCEU O JOGO!".format(Player2.nome))
                print("\n==============================\n")
                print("{:s} PERDEU O JOGO!".format(Player1.nome))
                print("\n==============================\n")
                break

            elif (Player2.Vida <= 0) and (Player2.Vida < Player1.Vida):
                print("\n==============================\n")
                print("{:s} VENCEU O JOGO!".format(Player1.nome))
                print("\n==============================\n")
                print("{:s} PERDEU O JOGO!".format(Player2.nome))
                print("\n==============================\n")
                break

            print("STATUS PLAYER1\n NICK: {:s}\n PERSONAGEM {:s}\n ESPÉCIE: {:s}\n VIDA: {:d}\n FORÇA: {:d}".format(
                Player1.nome, Player1.Tipo, Player1.Especie, Player1.Vida, Player1.Força))

            print("\n==============================\n")

            print("STATUS PLAYER2\n NICK: {:s}\n PERSONAGEM {:s}\n ESPÉCIE: {:s}\n VIDA: {:d}\n FORÇA: {:d}".format(
                Player2.nome, Player2.Tipo, Player2.Especie, Player2.Vida, Player2.Força))

            input("\nPressione enter para continuar...")
            os.system("cls")

    elif decisao == 3:
        msg = input("Digite sua mensagem:")
        Player1.conversar(Player2, msg)

    elif decisao == 4:
        break

    else:
        print("OPÇÃO INVÁLIDA")
        decisao = input("DESEJA CONTINUAR? S/N\nDIGITE -->")

        if (decisao == 'S') or (decisao == 's'):
            True
            os.system("cls")
        else:
            os.system("cls")
            break
