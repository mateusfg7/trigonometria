# BIBLIOTECAS
from lei_dos_cossenos import *

try:

    print("\n❪TRIGONOMETRIA❫")
    print("\n⎛1⎠ Lei dos Cossenos")
    res = input("\n❯ ")
    if res == "1":
        lei_cos()
    else:
        print("Opção inválida!")

except KeyboardInterrupt:
    print('\nSaindo...\n')
    exit()