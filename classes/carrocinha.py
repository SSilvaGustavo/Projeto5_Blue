from random import randint
from time import sleep
from classes.PePaTe import PePaTe
from classes.dados import Dados
from auxiliar.funcoes_auxiliares import final
class Carrocinha:

    # Pegando parametros relogio e personagem, para usar no main
    def carrocinha(self, relogio, personagem):
        print(f'Entre as ruas {personagem.nome} acaba se deparando com uma carrocinha')

        pepate = PePaTe()
        dado = Dados()
        escolha = int(input(''' 
        1 - Fugir
        2 - Esconder
        Escolha: ''')) #Escolha do usuario para as seguintes opções
        if escolha == 1: #Escolha Fugir
            sorteio_carrocinha = randint(1,2) #Sorteia um número para validação
            if sorteio_carrocinha == 1: #Cao conseguiu fugir
                relogio.avanca_tempo(80)
                print(f'{personagem.nome} corre apressado entre as ruas, fugindo do carro da carrocinha e daquele homem uniformizado que insiste em tentar laçar seu pescoço. Entre os becos encontra um lugar seguro e depois de uma longa perseguição se sente exausto e assustado.')
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                relogio.avanca_dia()
            elif sorteio_carrocinha == 2:  # Cao não conseguiu fugir
                print(
                    f'{personagem.nome} {personagem.nome} corre desesperadamente para se safar, passando correndo entre as pessoas que somente observam a cena, ele(a) implora ajuda, entretanto ninguém faz nada, somente observa a situação. Ele(a) corre para uma rua estreita na esperança de se esconder, entretanto não há saida e nosso amigo(a) é capturado pelo homem uniformizado')
                # Random para decidir se o cão foi doado
                adocao = randint(1, 5)
                while True:
                    print(
                        f"{personagem.nome} se debate desesperamente em vão. Entretanto agora você tem a chance de ajudar nosso amigo!!!")
                    teste = str(
                        input(f"\nVocê quer ajudar a criar uma distração, para ajudar {personagem.nome} a tentar fugir novamente [S/N]: ")).strip().upper()[0]
                    if teste == "S":
                        print(f'\nEntão jogue Jokenpo com o homem uniformizado e tente ajuda {personagem.nome}!')
                        # Jogo Pedra Papel e Tesoura atribuida a opção Fugir
                        pepate.jogopepate(personagem)
                        if pepate.jogadaCao == True:
                            relogio.avanca_tempo(80)
                            print(f'Deu certo!!! Você conseguiu criar uma distração e ajudar {personagem.nome}. E agora nosso(a) amigo(a) foge o mais rápido do que pode. Ele(a) precisa se esconder e se acalmar depois desse susto')
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            relogio.avanca_dia()
                            break
                    else:
                        print(f"Nem sempre com agilidade e malandragem das ruas é fácil conseguir fugir,apesa de muita luta, {personagem.nome} é levado para uma gaiola apertada da carrocinha, cheio de medo chora assustado")
                        personagem.muda_lugar('carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-10)
                            personagem.muda_humor(-10)
                            personagem.muda_frio(-5)
                            relogio.avanca_tempo(720)
                            print(f'''As horas se arrastam e {personagem.nome} não tem noção alguma de quanto tempo já está preso. O medo toma conta do seu coração, preso naquele lugar pequeno e frio ja não sabe o que pode fazer para fugir. Olha para os lados e ve gaiolas e mais gaiolas empilhadas cheias de cachorros, de varias tamanhos, alguns velhos, outros doentes, mas também alguns pequenos filhotes que parecm ter meses de vida.{personagem.nome} vendo isso pensa, " como pode existir um lugar tão triste como esse?" 
                                Os minutos continuam a passar se transformando em horas e mais horas, algumas vezes os homens uniformizados abrem as gaiolas para limpar as sujeiras e levar um pouco de ração seca, que nem se da vontade de comer, e é num desses momentos em que nosso amigo(a) ve uma oportunidade para fugir...
                                O homem uniformizado entra pela porta e a deixa encostada, vai limpando as gaiolas e colocando as comidas, quando tira o jornal sujo da gaiolo e se vira para jogar no lixo, {personagem.nome} aproveita e pula de dentro da gaiola e corre para a porta a fora. Começa uma gritaria e correria atras, mas nosso amigo corre desesperamente em busca da liberdade.''') 
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao != 1:
                                print(f'\n{personagem.nome} fica preso sem ter noção de quantas horas ja se passaram, seu coração está acelerado, com muito medo e frio seu rabo se encontra baixo, ele presta atenção a cada barulho com medo do que possa acontecer. Depois de algum tempo a porta se abre e outro homem uniformizado entra e lhe coloca um pote de ração seca, {personagem.nome} esta tão assuatado que nem tem vontade de comer, mesmo porque a comida nem tem um cheiro bom, na verdade ela não tem cheiro de nada, e nosso amigo choro com medo ficar preso ali para sempre.\n')
                                sleep(1)
                                print(f'Mais algumas horas se passam, e aquele lugar começa a ficar mais frio e escuro, {personagem.nome} já não tem mais esperanças... E mais uma vez a porta é aberta e entra o homem uniformizado, mas desta vez seguido de um rapaz. Eles estão passando pelas gaiolas falando sobre a quanto tempo cada um dos cães estão presos, "essa aqui ja esta a 4 semanas, esse outro aqui esta a a 2 semanas foram os donos que deixaram aqui pq iam se mudar, esse outro encontramos vagando nas ruas, mas é bem velho", segue o homem uniformizado falando. O corção do nosso amigo perde totalmente a esperança, até que o jovem rapaz se aproxima de sua gaiola, "Hey menino(a) venha cá!". {personagem.nome} se encolhe ainda mais no canto, com medo do que possa acontecer, entretatando puxam a coleira dele, e nosso(a) ve um rosto familiar ali, lembra vagamente de uma visita que fez no centro onde ganhou uma coxinha incrível desse rapaz, essa memoria vagou na memória de nosso(a) amiga(o) que nem percebeu que eles ja estavam fechando a porta e partindo, novamente tudo fica silencioso e frio....')
                                sleep(1)
                                print(f'''Logons minutos se passam e novamente a porta se abre,{personagem.nome} sem nenhuma emoção é arrastado para fora de sua jaula e é levado para fora da sala, vários olhinhos o acampanham até saída, e a porta se fecha.
                                Quando {personagem.nome} abre os olhos esta numa sala clara e o mesmo rapaz que lhe deu a coxinha estava lá, pega sua coleira e diz "Eu spu Pedro e agora você será parte da minha família, estou de adotando, se prepare porque agora temos que lhe dar um novo nome.''')
                                sleep(1)
                                final()
                                exit()
                            else:
                                print(f'''As horas se arrastam e {personagem.nome} não tem noção alguma de quanto tempo já está preso. O medo toma conta do seu coração, preso naquele lugar pequeno e frio ja não sabe o que pode fazer para fugir. Olha para os lados e ve gaiolas e mais gaiolas empilhadas cheias de cachorros, de varias tamanhos, alguns velhos, outros doentes, mas também alguns pequenos filhotes que parecm ter meses de vida.{personagem.nome} vendo isso pensa, " como pode existir um lugar tão triste como esse?" 
                                Os minutos continuam a passar se transformando em horas e mais horas, algumas vezes os homens uniformizados abrem as gaiolas para limpar as sujeiras e levar um pouco de ração seca, que nem se da vontade de comer, e é num desses momentos em que nosso amigo(a) ve uma oportunidade para fugir...
                                O homem uniformizado entra pela porta e a deixa encostada, vai limpando as gaiolas e colocando as comidas, quando tira o jornal sujo da gaiolo e se vira para jogar no lixo, {personagem.nome} aproveita e pula de dentro da gaiola e corre para a porta a fora. Começa uma gritaria e correria atras, mas nosso amigo corre desesperamente em busca da liberdade.''') 
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-10)
                                personagem.muda_humor(-10)
                                personagem.muda_frio(-5)
                                relogio.avanca_tempo(720) #12h após sair da carrocinha 
                                break
                                
        elif escolha == 2:#Escolha Esconder
            sorteio_carrocinha = randint(1,2) #Sorteia um número para validação
            if sorteio_carrocinha == 1:#Conseguiu se esconder
                relogio.avanca_tempo(80)
                print(f'{personagem.nome} corre sem rumo entra as ruas, sem se atrever a olhar para tras, corre tanto que suas pernas estavam ja cansadas e tremendo, desesperado procura um lugar seguro para que possa se esconder até a situação acalmar, entre os becos encontra uma casa abandonada com uma fresta quebrada na porta, e com esforço, rastejando consegue entrar e ficar seguro até que a poiera baixe.')
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(5)
            elif sorteio_carrocinha == 2: #Não conseguiu se esconder
                print(f'{personagem.nome} corre assustado entre os carros, desesperado não tem ideia onde esta e como pode se esconder. Mas logo atras esta os homens uniformizados o perseguindo novamente e conseguem alcança-lo antes de conseguir se esconder...\n''')
                sleep(1)
                adocao = randint(1,4)
                while True:
                    teste = str(input(f'Agora você tem a chance de ajudar nosso(a) amigo(a) criando uma distração para ele fugir. Você deseja tentar ajudar {personagem.nome} a fugir para se  esconder? [S/N]: ')).strip().upper()[0]
                    if teste == "S": 
                        dado.jogoDado(personagem)#Jogo do Dado atribuida a opção Esconder
                        if dado.caoDado == True:
                            relogio.avanca_tempo(80)
                            print(f'Após a sua distração, {personagem.nome} consegue fugir apressadamente entre os carros e depistar os homens uniformizados e ainda muito assustado busca refugiu entre os carros abandonados de um pátio abandonado.\n')
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-15)
                            personagem.muda_humor(-5)
                            break
                    else:
                        print(f'Apesar de tudo {personagem.nome} não consegue fugir da perseguição dos homens uniformizados e novamente é preso na gaiola fria da carrocinha')
                        personagem.muda_lugar('carrocinha')
                        if relogio.dia == 1: #Se o dia for igual a 1 o cachorro nao tem a opção de ser adotado (apenas a partir do dia 2)
                            personagem.muda_fome(-10)
                            personagem.muda_energia(-10)
                            personagem.muda_humor(-10)
                            personagem.muda_frio(-5)
                            relogio.avanca_tempo(720) #12h após sair da carrocinha
                            break
                        if relogio.dia > 1: #Depois do dia 1 o cachorro pode ser adotado
                            if adocao != 1:
                                print(f'As horas se passam lentas, e {personagem.nome}, já não tem mais esperanças, muito menos em uma fuga e segue com o rabinho baixo de tamanha a tristeza que esta no seu coração. A claridade se dá somente quando a porta é aberta para troca dos jornais e entrega das comidas. {personagem.nome} olha a sua volta e ve pilhas de gaiolas com cachorros amontoados, triste e doentes, completamente sozinhos e sem esperança, o que o deixa ainda mais amargurado, sem saber o que fazer...')
                                print(f'{personagem.nome} percebe que algumas vezes aparecem pessoas que levam alguns desses cachorros, não entende o porque só sabe que eles nunca mais voltam, o que o deixa ainda mais assustado.')
                                relogio.avanca_tempo(120) 
                                sleep(1)
                                print(f'Mais algum tempo passa e mais tres pessoas entram nas salas, algumas tentam passar a mão nos cachorros pela gaiola outras chamam, "pequeno vem aqui, toto olha aqui", {personagem.nome} não entende o que esta acontecendo. Uma menina se aproxima da gaiola e o(a) chama, "Vem aqui", um pouco receioso(a) {personagem.nome} se aproxima e cheira sua mão, mas a menina é puxada para longe da gaiola e a porta se fecha novamente. Mais uam vez nosso(a) amigo se encontra sozinho(a) e triste.')
                                sleep(1)
                                print(f' Mais uma vez a porta se abre e uma pessoa uniformizada entra e leva {personagem.nome} para fora da sala, la ele ve as pessoas que a pouco estavam olhando as gaiolas inclusive a menina que ele cheirou a mão, que corre em sua direção e o abraça dizendo que agora é parte da família.')
                                sleep(1)
                                final()
                                exit()
                            else:
                                personagem.muda_fome(-10)
                                personagem.muda_energia(-10)
                                personagem.muda_humor(-10)
                                personagem.muda_frio(-5)
                                relogio.avanca_tempo(720)
                                break
