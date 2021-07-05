from random import randint
from time import sleep

class PePaTe:
    def __init__(self):
        self.jogadaCao = True

    def jogopepate(self):
        pedra = '''  `.--.`                 
                    .+sss+/::/oss-              
            .++/oyo-     `.   `h+             
            .ho-sh-         `/+oooNso+:`        
        `m- ho                `.` `:h/       
        so /h /ssss+                `N       
        `N` m: +:.`                 .yo       
        .N `M` -:/osss:        -/+ooyd-       
        yo`M``oys/.                 .N`      
            /osh`   -/`                `N`      
            -h/                  ``:h/       
                /yo.          `-/++dh:`        
                .+ss+:.`      .:sy`          
                    `:/+osoooo+:`            
                                                
                                                '''
        tesoura = '''  
        `//+++///////++.            
        :s.+o.      `- `s:           
        :s`y--++/`    `//+h/:--.`     
        h s-`++-`           `.--://+: 
        o+d /o--+:                  +/
        +/  :-        .:/+yy+/////o-
        +o`               `/++.    
            `++-     `-//:`      :s.  
            -///////+/.:++/.   `h  
                            :++/o-  
                            '''
        papel = '''

                        .+///+-       
            ``        `++`   /+       
        //:://`    -o.   .o:`-//:.  
        o:   -s  -+:    /y+/:-  `/o 
        `s-   h:+:    `oo-`   `.:+- 
        .y   --     `/`    -//:-`  
        :+              `:ss+/:::+:
        -y:  --  `      `/.`   .-:+:
        `y/o`+:-/+-         -://:.`  
        y./o`/////`     -//-``      
        `o/.o/-.`   .:/+-`          
            .+/+s/////-`              
        '''
        escolha = " " #Escolha do usuario

        print("\n\033[3;7mBEM VINDO AO FAMOSO JOGO DO PEDRA, PAPEL OU TESOURA, OU PARA OS INTIMOS O FAMOSO JOKENPÔ, VAMOS JOGAR!\033[0;0m\n")
        escolha = str(input("Qual sua escolha? \033[1;30m[PE - PEDRA]\033[0;0m \033[1;37m[PA - PAPEL]\033[0;0m \033[1;33m[TE - TESOURA]\033[0;0m: ")).strip().upper()[0:2]
        maquina = randint(1,3) #Escolhe um número aleatoria de 1 a 3. 1 = Pedra 2 = Papel, 3 = Tesoura
        sleep(0.8)
        if escolha in "PE": #IF para Pedra
            print("\n\033[4;93mPEDRA", end=" ")
            sleep(0.7)
            print("PAPEL", end=" ")
            sleep(0.7)
            print("TESOOOOU", end="")
            sleep(1)
            print("RA\n\033[0;0m")
            if maquina == 1:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {pedra}''')
                print(f'''ESCOLHA DA MAQUINA:
                {pedra}''')
                print("\n\033[4;36mDESSA VEZ FOI EMPATE!\033[0;0m")
            elif maquina == 2:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {pedra}''')
                print(f'''ESCOLHA DA MAQUINA:
                {papel}''')
                print("\n\033[4;31mVOCÊ PERDEU! QUE AZAR\033[0;0m")
                self.jogadaCao = False
            else:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {pedra}''')
                print(f'''ESCOLHA DA MAQUINA:
                {tesoura}''')
                print("\n\033[4;32mVOCÊ GANHOU! PARECE QUE VOCÊ ESTÁ COM SORTE\033[0;0m")
                self.jogadaCao = True

        if escolha in "PA": #If para Papel
            sleep(0.6)
            print("\n\033[4;93mPEDRA", end=" ")
            sleep(0.7)
            print("PAPEL", end=" ")
            sleep(0.7)
            print("TESOOOOU", end="")
            sleep(1)
            print("RA\n\033[0;0m")
            if maquina == 1:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {papel}''')
                print(f'''ESCOLHA DA MAQUINA:
                {papel}''')
                print("\n\033[4;36mDESSA VEZ FOI EMPATE!\033[0;0m")
            elif maquina == 2:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {papel}''')
                print(f'''ESCOLHA DA MAQUINA:
                {tesoura}''')
                print("\n\033[4;31mVOCÊ PERDEU! QUE AZAR\033[0;0m")
                self.jogadaCao = False
            else:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {papel}''')
                print(f'''ESCOLHA DA MAQUINA:
                {pedra}''')
                print("\n\033[4;32mVOCÊ GANHOU! PARECE QUE VOCÊ ESTÁ COM SORTE\033[0;0m")
                self.jogadaCao = True

        if escolha in "TE": #If para Tesoura
            sleep(0.6)
            print("\n\033[4;93mPEDRA", end=" ")
            sleep(0.7)
            print("PAPEL", end=" ")
            sleep(0.7)
            print("TESOOOOU", end="")
            sleep(1)
            print("RA\n\033[0;0m")
            if maquina == 1:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {tesoura}''')
                print(f'''ESCOLHA DA MAQUINA:
                {tesoura}''')
                print("\n\033[4;36mDESSA VEZ FOI EMPATE!\033[0;0m")
            elif maquina == 2:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {tesoura}''')
                print(f'''ESCOLHA DA MAQUINA:
                {pedra}''')
                print("\n\033[4;31mVOCÊ PERDEU! QUE AZAR\033[0;0m")
                self.jogadaCao = False
            else:
                sleep(0.3)
                print(f'''SUA ESCOLHA:
                {tesoura}''')
                print(f'''ESCOLHA DA MAQUINA:
                {papel}''')
                print("\n\033[4;32mVOCÊ GANHOU! PARECE QUE VOCÊ ESTÁ COM SORTE\033[0;0m")
                self.jogadaCao = True