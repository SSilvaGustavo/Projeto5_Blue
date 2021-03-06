from random import randint
from time import sleep

try:
    from rich import print
except ModuleNotFoundError:
    print(f'''Você precisa do módulo 'rich' para rodar o programa!
              Terminal: pip install rich      
           ''')

from classes.carrocinha import Carrocinha
from rich.prompt import Prompt # Pra mudar a cor no input

from auxiliar.funcoes_auxiliares import final # importando a função latido
from auxiliar.funcoes_auxiliares import latido, cao_hostil, cao_correndo1, cao_amigo, cao_chorando2, cachorro_chorando, cao_correndo2
from auxiliar.funcoes_auxiliares import latido_inicio, opcoes_padrao
from auxiliar.validacoes import validar_input 

def fase1(relogio, personagem):
    print(f'\nSão {str(relogio)}, do {relogio.dia}° dia, {personagem.nome} encontra-se em um {personagem.lugar}.')
    print(personagem)
    sleep(1)
    latido_inicio()  # Chamando a função latido
    acao1 = int(Prompt.ask(f'''
    O que {personagem.nome} vai fazer?
    [blue]
    1- Procurar comida
    2- Procurar alguém para brincar
    3- Procurar um abrigo
    4- Voltar a dormir
    [/blue]
    '''))

    validar_input(acao1, [1, 2, 3, 4], relogio, personagem)

    opcoes_padrao(relogio, personagem, acao1)
    sleep(1)
    fase2(relogio, personagem, acao1)


def fase2(relogio, personagem, opcao_escolhida1): #Aprensenta a escolha, e a situação atual do cão
    print(
        f'São {str(relogio)}, {personagem.nome} você está em um {personagem.lugar}.')
    print(personagem)
    carrocinha = Carrocinha()
    if opcao_escolhida1 != 1:
        print('[blue]1- Procurar comida[/blue]')
    if opcao_escolhida1 != 2:
        print('[blue]2- Procurar alguém para brincar[/blue]')
    if opcao_escolhida1 != 3:
        print('[blue]3- Procurar um abrigo[/blue]')
    if opcao_escolhida1 != 4:
        print('[blue]4- Voltar a dormir[/blue]')
    print('[blue]5- Explorar a região[/blue]')

    acao2 = int(input('\nQual será sua próxima ação?\n'))
    
    validar_input(acao2, [1, 2, 3, 4, 5], relogio, personagem)
    
    opcoes_padrao(relogio, personagem, acao2)
    if acao2 == 5: #Condição que define randomicamente o local onde o Cão irá explorar 
        sorteio_passeio = randint(1, 4) #Random que define qual o destino do cão
        relogio.avanca_tempo(120)
        if sorteio_passeio == 1:
            personagem.muda_lugar("parque") #Random parque
            print(f'"Uma volta no parque sempre é uma boa ideia", pensa {personagem.nome}...')
            cachorro_hostil = randint(1, 3) #Random de escolha para validar o sucesso ou fracasso do personagem
            if cachorro_hostil == 1:
                cao_amigo()
                print(f'Esses passeios no parque são produtivos, pois {personagem.nome} consegue se alongar, correr e se divertir, mesmo sozinho(a). Às vezes ele(a) se aproxima de pessoas que dão algum petisco, ou até mesmo carinhos, outras o(a) espantam, ou se afastam assustadas. Mas observando as famílias com seus filhos e pets ele(a) ainda consegue ter esperança no fundo do coração de um dia ter alguém para coçar sua barriga e leva-lo(a) para um lar.')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(-5)
                personagem.muda_humor(10)
                print()
            elif cachorro_hostil == 2:
                latido()
                print(f'{personagem.nome} adora parques, fica correndo entre os arbustos e se esfregando na grama ele(a) brinca feliz, e acaba até se esquecendo da vida, e da tristeza de sempre estar sozinho(a). E no meio de tanta diversão não nota a presença de um cachorro hostil que o(a) observava, e que sem ao menos dizer uma palavra corre para atacar {personagem.nome}, que consegue se desvencilhar e corre para se esconder nos arbustos.')
                print()
                personagem.muda_fome(5)
                personagem.muda_energia(-5)
                personagem.muda_humor(5)
                print()
                if relogio.dia >= 2:
                    latido()
                    print(f'{personagem.nome} fica escondido até perceber que está novamente seguro, entretanto quando tenta sair dos arbustos sente uma mão lhe segurando, com cuidado uma mulher lhe pega no colo e fala baixinho: "Calma amiguinho(a) agora está tudo bem, eu vi o que aconteceu, ele não vai te morder, eu vou te proteger", e abraça {personagem.nome} carinhosamente, e segue em direção a saída do parque. {personagem.nome} nem pode acreditar no que está acontecendo, agora enfim vai ter oportunidade de ter um lar e uma família. ')
                    sleep(1)
                    final()
                    exit()
            else:
                cao_hostil()
                print(f'Esses passeios no parque são produtivos, pois {personagem.nome} sempre consegue umas migalhas das pessoas que estão fazendo piquenique, além de conseguir revirar os lixos e pegar as sobras, exceto quando os guardas o(a) expulsam antes. Mas dessa vez deu certo, já de barriguinha levemente cheia, ele(a) decide voltar para encontarar um lugar para descansar, entretanto uma carrocinha o(a) avistou e começou a persegui-lo(a)')
                print()
                personagem.muda_fome(5)
                personagem.muda_energia(5)
                personagem.muda_humor(-10)
                print()
                carrocinha.carrocinha(relogio, personagem)
        elif sorteio_passeio == 2:
            personagem.muda_lugar("shopping") #Random shopping
            shopping_passeio = randint(1, 3) #Random de escolha para validar o sucesso ou fracasso do personagem
            print(f'Talvez pudesse ir para a zona sul da cidade para conhecer, pois dizem que são granfinos quem vivem lá. "Talvez eu consiga algum petisco delicioso", pensa {personagem.nome}.')
            if shopping_passeio == 1:
                latido()
                print(f'Saindo dos becos escuros, ele(a) se dirige para o centro. Prédios altos, carros e muito barulho. Na esquina ele(a) avista um prédio muito grande e com um delicioso cheiro e corre naquela direção. Aquele seria o famoso Shopping, ele(a) tenta de todas as formas entrar, entretanto é barrado pelos seguranças, e resolve somente ficar sentado admirando a grandeza daquele lugar. Até que um rapaz se aproxima e faz um afago em sua cabeça, isso deixa {personagem.nome} muito feliz, ele(a) fica mais uns minutos e resolve voltar, hoje já ganhou um carinho, pensa nosso amigo com a barriga ja roncando, mas quando ele está em retirada o rapaz que lhe fez uma afago volta e lhe da uma coxinha. Realmente foi um dia de sorte. {personagem.nome} nunca tinha comido algo tão maravilhoso.')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                print()
            elif shopping_passeio == 2:
                latido()
                print(f'Entre as ruas movimentadas da cidade {personagem.nome} se assusta coma quantidade de carros que encontra, e acaba quase sendo atropelado(a), não é fácil caminhar entre tantos carros e pessoas. Entretanto {personagem.nome} avista um grande prédio onde lê a palavra "Shopping", sem ter ideia do que é ele(a) se aproxima e logo é barrado(a) pelos seguranças. Mas perto da porta uma família está parada brincando com bolas e nosso(a) amigo(a) se distrai com a cena. Uma das bolas cai perto dele e no mesmo momento a família entra num carro e deixam a bola para trás. {personagem.nome} se aproxima e pega a bola, joga para o alto e volta a pegar novamente, brincando feliz, com seu rabo em ritmo frenético. Entretanto em uma das jogadas a bola cai e sai rolando para longe e acaba entrando no bueiro, infelizmete não se tem nada o que nosso(a) amigo(a) possa fazer para recupera-la. "Mas a brincadeira foi boa, foi um dia de sorte", pensa nosso(a) amigo(a). ')
                print()
                personagem.muda_fome(5)
                personagem.muda_energia(5)
                personagem.muda_humor(5)
                print()
                if relogio.dia >= 2:
                    cao_correndo1()
                    print(f'{personagem.nome} decide voltar tranquilamente depois de toda a brincadeira, entretanto um carro para e desce uma família, sem entender um homem se aproxima e o(a) pega no colo, e nosso(a) amigo(a) percebe que é a família que deixou a bola, ele tenta desesperamente fugir pensando que eles vão castiga-lo por causa da bola que ele perdeu, mas o homem aos poucos tenta fazer um carinho e acalma-lo(a), em seguida o(a) coloca no banco de tras juntos com as crianças e diz: "Calma aminguinho(a) vamos para casa, agora esta tudo bem", pela primeira vez em muito tempo ele(a) se sentiu seguro, fechou os olhos e relaxou no banco do carro ')
                    sleep(1)
                    final()
                    exit()
            else:
                cao_chorando2()
                print(f'{personagem.nome} corre em sentido ao centro na expectativa de explorar outros lugares, parando entre uma moita e outra para fazer xixi ele(a) chega a um grandioso prédio onde de cara é barrado por seguranças, dizem que ele(a) não pode entrar no Shopping, e {personagem.nome} não tem nem ideia do que eles estão falando, "O que será esse tal de shopping?" pensa nosso(a) amigo(a). Entretanto mal dá tempo de admirar, pois os seguranças o(a) espantam para a rua e bem nessa hora aparece a carrocinha.')
                print()
                personagem.muda_fome(5)
                personagem.muda_energia(-5)
                personagem.muda_humor(-5)
                print()
                carrocinha.carrocinha(relogio, personagem)
        elif sorteio_passeio == 3:
            print(f'"Padaria é uma boa", pensa {personagem.nome} com agua na boca somente com a recordação de um dia que ganhou um pãozinho recheado.')
            print()
            personagem.muda_fome(10)
            personagem.muda_energia(-5)
            personagem.muda_humor(10)
            print()
            personagem.muda_lugar("padaria") #Random padaria
            surpresa = randint(1,3) #Random de escolha para validar o sucesso ou fracasso do personagem
            if surpresa == 1:
                cao_correndo1()
                print(f'{personagem.nome} corre na padaria na expectativa de ganhar alguma coisa para comer, qualquer coisa é bem vinda, pois as vezes ele(a) fica dias sem comer, então precisa aproveitar todas as oportunidades. Chegando lá seu antigo amigo padeiro o vê, e entra fechando a porta, "Talvez hoje ele esteja de mal humor, ou se esqueceu de mim?", pensa nosso(a) amigo(a). Mas um minuto depois o gentil padeiro aparece com um delicioso pão com mortadela e enrola um pano no pescoço do nosso(a) amigo(a), o gentil padeiro disse que era um cachecol para mante-lo(a) aquecido(a). {personagem.nome} come num piscar de olhos e parte todo(a) feliz e agradecido(a)')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                personagem.muda_frio(20)
                print()
            elif surpresa == 2:
                latido()
                print(f'{personagem.nome} sabe alguns lugares para conseguir comida, ainda existem pessoas gentis que o(a) alimentam às vezes, mas existe épocas que fica dias sem comer, tendo que tomar água dos córregos, ou a água com sabão que as pessoas lavam o quintal e fica parada nas ruas. "Talvez hoje eu tenha sorte e ganhe um petisco gostoso", pensa nosso(a) amigo(a) enquanto corre para a padaria. Quando chega lá encontra o velho padeiro que esta na janela, e como de costume joga uns petisquinhos de frios para {personagem.nome} que agora parte feliz e com a barriguinha cheia. Entretanto ao virar a esquina ele ve a carrocinha que começa a persegui- lo(a)') 
                print()
                personagem.muda_fome(5)
                personagem.muda_energia(-5)
                personagem.muda_humor(10)
                print()
                carrocinha.carrocinha(relogio, personagem)
            else:
                cachorro_chorando()
                print(f'{personagem.nome} corre para a Padaria em busca de alguns petiscos, parando só para fazer xixi em algumas moitas para dizer que passou por lá, mas quando chega na padaria a porta está fechada, e está cheio de gente. Ele(a) tenta se aproximar mas as pessoas gritam com ele(a) e o mandam sair."Infelizmente hoje não é um dia de tanta sorte," pensa nosso(a) amigo(a).')
        else:
            personagem.muda_lugar("açougue") #Random açougue
            sorteioacougue = randint(1, 3) #Random de escolha para validar o sucesso ou fracasso do personagem
            if sorteioacougue == 1:
                print(f' {personagem.nome} continua entre as ruas deixando seu nariz conduzir o caminho para algum lugar que possa ter algum petisco gostoso, até que se depara com um açougue.')
                print()
                personagem.muda_fome(15)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                personagem.muda_frio(10)
                print()
                if relogio.dia > 1:
                    adocao_acougue = randint(1,4) #Random de escolha para validar se o cão foi adotado APÓS o 2º Dia
                    if adocao_acougue != 1:
                        cao_correndo2()
                        print(f'{personagem.nome}, fica parado(a) admirando as carnes na vitrine do açougue, com a boca salivando de tamanha a vontade, entretanto não se atreve a entrar, ja esta cansado(a) demais para ter que fugir quando for enxotado(a). Ele(a) fica parado(a) ali observando e pensando que a vida as vezes é muito difícil, e mal percebe um funcionário do açougue se aproximando com um osso gigante, e carinhosamente entrega a {personagem.nome} que começa a roer ali mesmo. Em seguida o tal funcionário se aproxima e senta ao lado do nosso(a) amigo(a) e começa a passar a mão na sua cabeça, bem devagarinho, a tempos {personagem.nome} não se sente tão acolhido(a) e se se acomoda mais perto do homem, que o pega e o leva para a parte de tras do açougue. {personagem.nome} não entende muito bem o que está acontecendo, em seguida o homem lhe entrega um cobertor e um potinho com água, lhe faz um afago e diz: "Acho que sua vida não é muito fácil amiguinho(a), as vezes não é a vida na rua é difícil e solitária... Agora você pode viver aqui porque você finalmente encontrou um lar, a partir de hoje eu sou sua companhia e você a minha"')
                        sleep(1)
                        final()
                        exit()
                    else:
                        latido()
                        print(f'{personagem.nome}, você encotrou um açougue. O dono era muito gentil e deixou você no açougue até o proximo dia!')
                        relogio.avanca_dia()
                        personagem.muda_lugar('beco')
            elif sorteioacougue == 2:
                latido()
                print(f'{personagem.nome}, você encontrou um açougue. O dono era muito gentil, porém deixou você ficar com ele apenas durante o dia!')
                print()
                personagem.muda_fome(10)
                personagem.muda_energia(10)
                personagem.muda_humor(10)
                personagem.muda_frio(10)
                print()
                relogio.avanca_tempo(720)
            else:
                cao_chorando2()
                print(f'{personagem.nome}, andando entre as ruas e becos seu nariz sente um cheiro gostoso no ar e se depara com um açougue, e ali fica a admirar as carnes, mas nem consegue se aproximar direito pois o açougueiro vem correndo o espantar com uma vassoura, e grita chamando a carrocinha dizendo: "Tem um(a) pulguento(a) aqui!". E pelo azar de nosso(a) amigo(a) eis que a carrocinha surge e começa a perseguição.')
                carrocinha.carrocinha(relogio, personagem)

    fase1(relogio, personagem)
