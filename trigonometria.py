from lei_dos_cossenos import *
from lei_dos_senos import *
from area_triangulo import *

try:

    print("\033[04mctrl+c para sair ou digite 'sair'/'exit'")
    print("\n\033[00;00;00m\033[01;31m❪\033[07;31mTRIGONOMETRIA\033[00;00;00m\033[01;31m❫")

    while True:
        
        print("\n\033[00;00;00m\033[01;31m⎛\033[07;31m1\033[00;00;00m\033[01;31m⎠ Lei dos Cossenos")
        print("\n\033[00;00;00m\033[01;31m⎛\033[07;31m2\033[00;00;00m\033[01;31m⎠ Lei dos Senos")
        print("\n\033[00;00;00m\033[01;31m⎛\033[07;31m3\033[00;00;00m\033[01;31m⎠ Área do triângulo")

        res = input("\n\033[07;31m❯\033[00;00;00m\033[01;31m ")

        if res == "1":
            lei_cos()
        elif res == "2":
            lei_sen()
        elif res == "3":
            area_tri()
        elif res == 'sair' or res == 'exit':
            print('\n\nSaindo...\n')
            exit()
        else:
            print("\n\033[07m\033[05;31mOpção inválida!")

except KeyboardInterrupt:
    print('\n\nSaindo...\n')
    exit()