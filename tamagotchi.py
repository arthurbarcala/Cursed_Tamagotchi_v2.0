import random
class Tamagotchi:
    def __init__(self):
        self.nome = ""
        self.dinheiro = 5
        self.fome = 5
        self.saude = 10
        self.idade = 0
        self.insanidade = 0

    def alterarNome(self, nome):
        self.nome = nome

    def alimentar(self):
        self.fome += 5

    def curar(self):
        self.saude += 5

    def envelhecer(self):
        self.idade += 1

    def calcularHumor(self):
        return (self.fome + self.saude)/2

    def retNome(self):
        return self.nome

    def retFome(self):
        return self.fome

    def retSaude(self):
        return self.saude

    def retIdade(self):
        return self.idade
    #funções de jogos/interação
    def brincar(self):
        while True:
            if self.saude >0:
                if (self.insanidade < 6):
                    print("Escolha uma brincadeira:")
                    resp = input("1 - jokenpo | 2 - contar histórias\n")
                    if resp == "0":
                        break
                    elif resp == "1":
                        self.jokenpo()
                    elif resp == "2":
                        self.historias()
                    else:
                        print("Opção inválida")
                else:
                    print("Escolha uma brincadeira:")
                    resp = input("1 - jokenpo | 2 - contar histórias | 666 - roleta RUSSA\n")
                    if resp == "0":
                        break
                    elif resp == "1":
                        self.jokenpo()
                    elif resp == "2":
                        self.historias()
                    elif resp == "666":
                        self.roletaRussa()
                    else:
                        print("Opção inválida")
            else:
                print("Há um cadáver por perto. Não é possível brincar...")
                break
            print("----------------------------------------------------------------")
    def jokenpo(self): ##4
        while True:
            print("Escolha pedra papel ou tesoura:")
            resp = input("1 - Tesoura | 2 - Pedra | 3 - Papel | 0 - Sair do jogo\n")
            if resp == "0":
                break
            if self.dinheiro > 0:
                if resp != "1" and resp != "2" and resp != "3" and resp != "0":
                    print("Opção inválida!!!")
                else:
                    jogador = int(resp)
                    oponente = random.randint(1, 3)

                    if jogador == 1:
                        print("Você escolheu Tesoura!")
                    elif jogador == 2:
                        print("Você escolheu Pedra!")
                    elif jogador == 3:
                        print("Você escolheu Papel!")
                    else:
                        print("Erro! Opção inválida")

                    if oponente == 1:
                        print("Oponente escolheu Tesoura!")
                    elif oponente == 2:
                        print("Oponente escolheu Pedra!")
                    elif oponente == 3:
                        print("Oponente escolheu Papel!")
                    else:
                        print("Erro! Opção inválida")

                    if jogador > oponente:
                        if oponente == 1 and jogador == 3:
                            print("Oponente ganhou!!")
                            print("Você perdeu 2 dinheiros..")
                            self.dinheiro -= 2
                            print(f"Você possui {self.dinheiro} dinheiros")
                        else:
                            print("Você ganhou!! Parabéns!!!")
                            print("Você ganhou 3 dinheiros!!!")
                            self.dinheiro += 3
                            print(f"Você possui {self.dinheiro} dinheiros!!!")
                    elif oponente > jogador:
                        if jogador == 3 and jogador == 1:
                            print("Você ganhou!! Parabéns!!!")
                            print("Você ganhou 3 dinheiros!!!")
                            self.dinheiro += 3
                            print(f"Você possui {self.dinheiro} dinheiros!!!")
                        else:
                            print("Oponente ganhou!!")
                            print("Você perdeu 2 dinheiros..")
                            self.dinheiro -= 2
                            print(f"Você possui {self.dinheiro} dinheiros")
                    else:
                        print("Empate!!")
            else:
                print("Você não tem dinheiro! Seu pobre fud***")
            print("------------------------------------------------------------------------------------")
    def historias(self):
        if self.insanidade == 0:
            print("O dia em que fui ao parque.")
            input()
            print("Certo dia, estava muito ensolarado e decidi ir ao parque...")
            input()
            print("Chegando lá, fiz vários amiguinhos!! ...")
            input()
            print("Brinquei muito!! Pega-pega, pique-esconde, cabra-cega!...")
            input()
            print("Foi muito legal!!!!!!!")
            print("--------------------------------------------------------------------")
            self.insanidade+=1
        elif self.insanidade == 1:
            print("Quando eu estava brincando de pega-pega...")
            input()
            print("Um dos meus amiguinhos foi me pegar...")
            input()
            print("Ele me empurrou muito forte...")
            input()
            print("Eu acabei caindo no chão e comecei a chorar, pois me machuquei...")
            input()
            print("Ele então disse para eu não chorar, me ajudou a levantar...")
            input()
            print("E até comprou um sorvete para mim!!!")
            input()
            print("Ficamos muito felizes!!!")
            print("--------------------------------------------------------------------")
            self.insanidade+=1
        elif self.insanidade == 2:
            print("No meio do caminho para casa, encontramos um cachorrinho...")
            input()
            print("Ele era muito fofo...")
            input()
            print("Fiz carinho nele, e ele lambeu minha mão...")
            input()
            print("Estávamos indo para casa e ele ficou nos seguindo alegremente...")
            print("--------------------------------------------------------------------")
            self.insanidade+=1
        elif self.insanidade == 3:
            print("Enquanto caminhávamos, tropecei em uma pedra...")
            input()
            print("Eu caí no chão")
            input()
            print("Meu 'amigo' riu de mim...")
            input()
            print("...")
            input()
            print("ELE RIU DE MIM!!!!!")
            input()
            print("ELE!!!!!!!!")
            input()
            print("...")
            input()
            print("ELE ME PAGA!!!!!!!!!!!!!!!!!!!!!!!")
            self.insanidade+=1
        elif self.insanidade == 4:
            print("Voltei para casa chorando...")
            input()
            print("Cheguei na cozinha...")
            input()
            print("Lá em cima... No armário...")
            input()
            print("Tem uma faca grande...")
            input()
            print("Pegue-a para mim.")
            print("1 - 'Não vou pegar. É perigoso.'")
            input()
            print("PEGUE-A!!!!!!")
            print("1- 'Não vou pegar!'")
            input()
            print("EU MANDEI VOCÊ PEGAR!!!!!!!!!!!!!!")
            input()
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa")
            input()
            print("PEGUE A MERDA DA FACA!!!!!!!!!!!!!")
            input()
            resp = input(f"1 - Fugir | 2 - Espancar {self.retNome()}\n")
            if resp == "1":
                print("*Você decidiu correr.*")
                input()
                print("*Você tropeçou na quina da estante e o tamagotchi te deu uma mordida.")
                input()
                print("MUITO. FORTE...")
            else:
                print(f"*Você decidiu bater muito forte em {self.retNome()}*")
            print(f"Você socou {self.retNome()} na cara tão forte que ele desmaia.")
            input()
            print("Finalmente você acorda. Foi tudo um sonho...")
            input()
            print("                                                                  -Ou será que não?")
            self.insanidade+=1
        elif self.insanidade == 5:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            input()
            print("          **********\n       ***          **\n    ****             **\n  ***                 *\n **   -----         ---**\n*         -----------   **\n*        ..        ..    *\n*        ..        ..     *\n**                        *\n **       ^^^^^^^^^     **\n  *****   ^vvvvvvv^    **\n        ***************")
            input()
            print(f"{self.retNome()} está puto e triste")
            input()
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            input()
            print("Me mate.")
            self.insanidade+=1
        elif self.insanidade == 6:
            print("Vá ao porão.")
            input()
            print("Eu MANDEI você ir.")
            input()
            print("1 - Ir ao porão")
            input()
            print("*Você chega no porão.*")
            input()
            print("1 - Acender a luz")
            input()
            print("-- Ugh! Que fedor!!")
            input()
            print("...")
            input()
            print("*Você vê uma massa nojenta em decomposição e fica em choque*")
            input()
            print("*Uma voz diz ao fundo:*")
            input()
            print("Muito fofinho, não é? ...")
            input()
            print("Meu cachorrinho...")
            input()
            self.insanidade+=1
        elif self.insanidade <= 7:
            print("Vamos ver quem tem mais sorte...")
            input()
            self.roletaRussa()

    def roletaRussa(self):
            numero = random.randint(1, 3)
            print("Inserindo uma bala... CLICK!")
            input()
            print("Girando o gatilho bem rápido...")
            input()
            print("DZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
            input()
            print(f"1 - Apertar gatilho em si mesmo | 2 - Atirar em {self.retNome()}")
            resp = input()
            if resp == "2":
                if numero == 3:
                    print("POW!!")
                    input()
                    print(f"{self.retNome()} foi morto. Agora você deve se virar com isso.")
                    self.saude -= 100
                else:
                    print("CLICK!")
                    input()
                    print("Ufa! todos estão vivos...")
            elif resp == "1":
                if numero == 3:
                    print("POW!!")
                    input()
                    print("Você se matou...")
                    self.saude -= 100
                    input()
                    print("POW!!")
                    input()
                    print("...")
                    input()
                    print(f"{self.retNome()} enlouqueceu e suicidou-se")
                else:
                    print("CLICK!")
                    input()
                    print("Ufa! todos estão vivos...")
            else:
                print(
                    "MORRA MORRA MORRA MORRA MORRAAAA MORRA MORRA MORRA MORRAMORRA MORRA MORRA MORRAMORRA MORRA MORRA MORRA\nMORRA MORRA MORRA MORRAMORRA MORRA MORRA MORRAMORRA MORRA MORRA MORRAMORRA MORRA MORRA MORRA")


#--------------------------------------------------------------------------------------------
tamagotchi1 = Tamagotchi()
print("Cursed Tamagotchi v2.0.0")
print("Aperte qualquer tecla para continuar:")
input()
nome = input("Insira um nome para teu Tamagotchi!\n")
tamagotchi1.alterarNome(nome)
while tamagotchi1.saude>0:
    print(f"{tamagotchi1.retNome()} está com {tamagotchi1.calcularHumor()} de humor.")
    print()
    print(
        "                ****\n              **    **\n           ** ^      ^ **\n        **    O      O	  **\n       *    ///   U   ///   *\n        *                  *\n         ******************")
    print()
    print("O que deseja fazer??")
    print()
    print("0 - Mate o teu bicho")
    print("1 - Altera o nome")
    print("2 - Alimenta teu bicho")
    print("3 - Cura teu bicho")
    print("4 - Brinque com teu bicho")
    resposta = input()

    if resposta != "1" and resposta != "2" and resposta != "3" and resposta != "4" and resposta != "0":
        resposta = 0
    else:
        resposta = int(resposta)

    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    if resposta == 0 or tamagotchi1.saude <= 0:
        print(
            "              ********\n           ** _      _ **    --{'MORRI'}\n        **    X      X	  **\n       *          O         *\n         ******************")

        print()
        print("Matou teu bicho!!!")
        print("MONSTRO DE MERDA")
        break
    elif resposta == 1:
        nome = input("Insira um nome para teu Tamagotchi!\n")
        tamagotchi1.alterarNome(nome)
        print(f"O nome de teu bicho é {tamagotchi1.retNome()}")
    elif resposta == 2:
        print("Bicho alimentado!!")
        tamagotchi1.alimentar()
        print(f"{tamagotchi1.retNome()} está com {tamagotchi1.retFome()} de comida")
    elif resposta == 3:
        print("Bicho curado!!")
        tamagotchi1.curar()
        print(f"{tamagotchi1.retNome()} está com {tamagotchi1.retSaude()} de saude")
    elif resposta == 4:
        tamagotchi1.brincar()
    else:
        print("Opção inválida!!!")
    tamagotchi1.envelhecer()
    if tamagotchi1.retIdade() > 10:
        tamagotchi1.fome -= 1
        tamagotchi1.saude -= 1
        print("Teu bicho envelheceu e perdeu 1 de saude")
        print(f"Saúde de {tamagotchi1.retNome()}: {tamagotchi1.retSaude()}")
        if tamagotchi1.retSaude() <= 0:
            print("Teu bicho morreu...")
            print("ESTÚPIDO!")
            break
        if tamagotchi1.retFome() <= 0:
            tamagotchi1.saude -= 1
            print("Teu bicho está faminto!!! Alimente-o")