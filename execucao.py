from time import sleep

from os import system

from lista import listaPergunta, listaResposta, listaPremio, listaJogadores, listaPontuacao

from random import randint

from copy import deepcopy

def jogo(): #função que faz as perguntas do jogo
    errou = False
    contador = 0
    parar = "n"
    contadorpulos = 0
    denovo = "t"
    system("cls")
    print(f"""
        ----------------------------------------------------------
                Olá {nome} vamos a primeira pergunta
        ----------------------------------------------------------
        ---A qualquer momento digite [j] para pular a pergunta----
        ----------------------------------------------------------
        """)
    if contadorpulos < 3:
        print(f"Lembando que você ainda tem { ( 3 - contadorpulos) } pulos")
        print()
    else:
        print(f"você não tem mais pulos")
        print()
    question = randint(0,(49-contador))

    print(listaPergunta[question])

    resposta = input("Sua resposta é: ").strip().lower()

    while resposta not in ("a","b","c","d","e","p","j"):
        resposta = input("""Resposta invalida.   Por favor digite uma resposta válida: """).strip().lower()

    if resposta == "p":
        parar = input(f"""Você deseja mesmo parar? [S/N]
        Se parar você sairá com R${(listaPremio[contador] * 1000)}
        r: """).strip().lower()

        while parar not in ("s","n"):
            parar = input(f"""Você deseja mesmo parar? [S/N]
            Se parar você sairá com {(listaPremio[contador] * 1000)}
            r: """).strip().lower()

        if parar == "s":
            system("cls")
            print(f"Parabéns você saiu com R${(listaPremio[contador] * 1000)}")
            while denovo not in ("s","n"):
                denovo = input(f"""Você deseja jogar novamente? [S/N]
                r: """).strip().lower()

            if denovo == "s":
                system("cls")

                listaJogadores.append(nome)

                listaPontuacao.append(contador)

                telainicial()

            else:
                print()
        else:
            print()
    elif resposta == "j":
        if contadorpulos >= 3:
            print("Desculpe você não tem mais pulos!")
        else:
            contadorpulos += 1

            contador += 1

            del listaPergunta[question]

            del listaResposta[question]

            system("cls")

    elif resposta != listaResposta[question]:
            system("cls")
            print(f"Que pena você errou e ficou com R${(listaPremio[contador] * 500)}")
            errou = True
            while denovo not in ("s","n"):
                denovo = input(f"""Você deseja jogar novamente? [S/N]
                r: """).strip().lower()

            if denovo == "s":
                system("cls")

                listaJogadores.append(nome)

                listaPontuacao.append(contador)

                telainicial()

            else:
                print()

    else:
        contador+=1

        print(f"Parabens você acertou e foi para pergunta de R${listaPremio[contador+1] * 1000}")

        sleep(2)

        del listaPergunta[question]

        del listaResposta[question]

        question = randint(0,(49-contador))

        system("cls")
    while errou == False and contador <15 and parar == "n":
        sleep(0.5)
        print(f"""
            ----------------------------------------------------------
            {nome} vamos a {contador+1}ª pergunta
            ----------------------------------------------------------
            ---------A qualquer momento digite [p] para parar---------
            ----------------------------------------------------------
            ---A qualquer momento digite [j] para pular a pergunta----
            ----------------------------------------------------------""")
        if contadorpulos < 3:
            print(f"Lembando que você ainda tem { (3 - contadorpulos) } pulos")
        else:
            print(f"você não tem mais pulos")

        print(listaPergunta[question])
        resposta = input("Sua resposta é: ").strip().lower()

        while resposta not in ("a","b","c","d","e","p","j"):
            resposta = input("""Resposta invalida.   Por favor digite uma resposta válida: """).strip().lower()

        if resposta == "p":
            parar = input(f"""Você deseja mesmo parar? [S/N]
            Se parar você sairá com R${(listaPremio[contador] * 1000)}
            r: """).strip().lower()

            while parar not in ("s","n"):
                parar = input(f"""Você deseja mesmo parar? [S/N]
                Se parar você sairá com {(listaPremio[contador] * 1000)}
                r: """).strip().lower()

            if parar == "s":
                system("cls")
                print(f"Parabéns você saiu com R${(listaPremio[contador] * 1000)}")
                while denovo not in ("s","n"):
                    denovo = input(f"""Você deseja jogar novamente? [S/N]
                    r: """).strip().lower()

                if denovo == "s":
                    system("cls")

                    listaJogadores.append(nome)

                    listaPontuacao.append(contador)

                    telainicial()

                else:
                    print()

                system("cls")
            else:
                print()
        elif resposta == "j":
            if contadorpulos >= 3:
                print("Desculpe você não tem mais pulos!")
            else:

                contadorpulos += 1

                contador += 1

                del listaPergunta[question]

                del listaResposta[question]

                system("cls")

        elif resposta != listaResposta[question]:
            system("cls")
            print(f"Que pena você errou e ficou com R${(listaPremio[contador] * 500)}")
            errou = True
            while denovo not in ("s","n"):
                denovo = input(f"""Você deseja jogar novamente? [S/N]
                r: """).strip().lower()

            if denovo == "s":
                system("cls")

                listaJogadores.append(nome)

                listaPontuacao.append(contador)

                telainicial()

            else:
                print()

            system("cls")

        else:
            contador+=1

            print(f"Parabens você acertou e foi para pergunta de R${listaPremio[contador+1] * 1000}")

            sleep(2)

            del listaPergunta[question]

            del listaResposta[question]

            question = randint(0,(49-contador))

            system("cls")
    if contador == 15:
        print(f"""
            ------------------------------------------------------------------------
               Olá {nome}, parabéns você chegou a pergunta de um milhão de reais!
            ------------------------------------------------------------------------
            -----------------Está pronto(a) para o tudo ou nada?--------------------
            ----------------Lembrando que se você errar perde tudo------------------
            ------------------------------------------------------------------------
            """)
        question = randint(0,(49-contador))

        print(listaPergunta[question])

        resposta = input("Sua resposta é: ").strip().lower()

        while resposta not in ("a","b","c","d","e","p"):
            resposta = input("""Resposta invalida.   Por favor digite uma resposta válida: """).strip().lower()

        if resposta != listaResposta[question]:

            system("cls")
            print("Que pena você errou e pedeu TUDO!")
            errou = True

            while denovo not in ("s","n"):
                denovo = input(f"""Você deseja jogar novamente? [S/N]
                r: """).strip().lower()

            if denovo == "s":
                system("cls")

                listaJogadores.append(nome)

                listaPontuacao.append(contador)

                telainicial()

            else:
                print()

            system("cls")

        else:
            contador+=1
            print("Parabéns você acaba de ganhar UM MILHÃO DE REAIS!! OH OH")
            while denovo not in ("s","n"):
                denovo = input(f"""Você deseja jogar novamente? [S/N]
                r: """).strip().lower()

            if denovo == "s":
                system("cls")

                listaJogadores.append(nome)

                listaPontuacao.append(contador)

                telainicial()

            else:
                print()

            system("cls")

def telainicial():#função que começa o jogo colocando nome e escolhendo jogar sair ou mostrar classificação
    global nome
    system("cls")
    print("""
                -------------------------------------------------------
                --------------Bem vindo ao Show do milhão--------------
                -------------------------------------------------------""")
    sleep(0.5)

    nome = input("Digite seu nome: ")

    while nome=="":#impedidno que o usuário coloque um nome em branco
        nome = input("Por favor, Digite um nome válido: ")
    system("cls")
    oquefazer()

def oquefazer():

    listaJogador = deepcopy(listaJogadores)

    listaPontos = deepcopy(listaPontuacao)

    rodando = 0
    opcao = "9"
    while opcao not in ("1","2","3"):#manter as respostas entre as 3 possiveis

        if rodando != 0:
            print("Opção inválida, por favor digite uma opção válida!")

        opcao = input(f"""Bem vindo {nome}, o que fazer?
                    Digite [1] para jogar!
                    Digite [2] para ver classificação!
                    Digite [3] para sair!

                    E tecle enter!
                    R: """).strip().upper()
        rodando+=1

    if opcao == "1":

        jogo()

    elif opcao == "2":
        system("cls")

        print('{:^30} {:^10} {:^10}'.format('Jogador', '-', 'Pontuação'))

        for pessoa in range(len(listaJogador)):

            print('-' * 50)

            print('{:^30} {:^10} {}{:<10}'.format(listaJogador[listaPontos.index(max(listaPontos))], '-', 'R$', (listaPremio[max(listaPontos)]*1000)))

            del listaJogador[listaPontos.index(max(listaPontos))]

            listaPontos.remove(max(listaPontos))


        print()

        print()

        input("Digite enter para voltar")

        telainicial()

    else:
        sair = input("Deseja mesmo sair? [S/N]").strip().lower()
        if sair=="s":
            print()
        else:
            oquefazer()
telainicial()
