import math # IMPORTA BIBLIOTECA DE CALCULOS MATEMÁTICOS

class lei_cos:

    def __init__(self):
    
        print("\n\033[00;36m❰\033[01;36mLEI DOS COSSENOS\033[00;36m❱\n")

        # PEGA OS VALORES NECESSÁRIOS
        try:
            val_um = float(input('\033[00;36mValor da reta adjacente 1 》 \033[01;36m'))
            val_dois = float(input('\033[00;36mValor da reta adjacente 2 》 \033[01;36m'))
            val_angulo = float(input('\033[00;36mÂngulo 》 \033[01;36m'))
        except ValueError:
            print("Valores inválidos!")
            exit()


        # CALCULA O QUADRADO DOS VALORES UM E DOIS
        val_um_quad = math.pow(val_um,2)
        val_dois_quad = math.pow(val_dois,2)

        # CONVERTE O ANGULO EM GRAUS PARA RADIANO
        val_angulo_rad = (val_angulo / 180) * math.pi

        # CALCULA O COSSENO DO ÂNGULO
        cos_angulo = math.cos(val_angulo_rad)
        cos_angulo_f = float('{:.2f}'.format(cos_angulo))


        # CALCULA O VALOR DE X
        x = math.sqrt(val_um_quad + val_dois_quad - 2 * val_um * val_dois * cos_angulo_f)

        # EXIBE O RESULTADO
        print('\nx \033[00;36m≅ \033[01;36m{:.2f}'.format(x))