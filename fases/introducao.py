from time import sleep

try:
    from tqdm import tqdm  # Importa a barra de carregamento#
except ModuleNotFoundError:
    print(f'''Você precisa do módulo 'tdqm' para rodar o programa!
              Terminal: pip install tdqm        
           ''')

try:
    from rich import print
except ModuleNotFoundError:
    print(f'''Você precisa do módulo 'rich' para rodar o programa!
              Terminal: pip install rich       
           ''')
           
from auxiliar.funcoes_auxiliares import print_delay
from auxiliar.funcoes_auxiliares import musica_incial # Importando a função da musica inicial




class Introducao:
    def __init__(self):
        pass

    def executar(self):
        musica_incial()  # Chamando a função da musica inicial
        print(f'''[blue]
           ,-.___,-.
           \_/_ _\_/
             )O_O(
            ( ( ) )
  ---------( )U-'( )----------
           ```   ```
       [blue] ''')
        print_delay('''
        Jogo - Dia de Cão 
       
Nesta trama você terá a oportunidade de conhecer o dia de um cão, o objetivo é ajudar um cachorro de rua a sobreviver e ser adotado,  enquanto foge de um grande inimigo, a carrocinha. 

Mas a vida nas ruas não é fácil, então fique atento nas necessidades do cão, pois se algum dos status zerarem, você precisará começar o jogo novamente para tentar ser um melhor companheiro para seu amigo.

 Humor - O humor é baseado nas escolhas que você ajudará o cão a tomar. O sucesso, e as falhas que acontecem influenciam diretamente, alterando o status.
 
 Fome - O nivel de fome, é atrelado a foma além de outros status. Então fique atento, e cuide para que não fique baixo nenhum deles.

 Frio - Nível de frio, também é modificado conforme determinadas situações, além da queda de temperatura não esqueça que tudo influencia outros status, isso quer dizer: "Um cachorrinho quente é um cachorro feliz."

 Energia - A energia são os pontos de ação, todas as suas atividades gastam energia, tente manter sua barriguinha cheia, e com status saudaveis. 

        ''')
        print(f'''[blue]

                                  .-.
     (___________________________()6 `-,
     (   __ Começando o Jogo __   /''"`
     //\\                      //\\
     "" ""                     "" ""
       [blue] ''')
        for i in tqdm(range (150)): #Cria um indicador de carregamento#
            sleep(0.0001)
        print()
        sleep(1)
       
