import math # IMPORTA A BIBLIOTECA DE CALCULOS MATEMÁTICOS

class lei_sen:

    def __init__(self):

        print("\n\033[00;36m❰\033[01;36mLEI DOS SENOS\033[00;36m❱\n")

        # PEGA OS VALORES NECESSÁRIOS
        try:
            val_reta_adj = float(input('\033[00;36mValor da reta adjacente 》 \033[01;36m'))
            val_ang_ops_reta = float(input('\033[00;36mValor do angulo oposto a reta adjacente 》 \033[01;36m'))
            val_ang_ops_x = float(input('\033[00;36mValor do angulo oposto a X 》 \033[01;36m'))
        except ValueError:
            print("Valores inválidos!")
            exit()


        # CONVERTE O ANGULO EM GRAUS PARA RADIANO
        val_rad_ops_reta = (val_ang_ops_reta / 180) * math.pi
        val_rad_ops_reta_f = float('{:.2f}'.format(val_rad_ops_reta))
        val_rad_ops_x = (val_ang_ops_x / 180) * math.pi
        val_rad_ops_x_f = float('{:.2f}'.format(val_rad_ops_x))

        # CALCULA O SENO DOS ANGULOS
        sen_ops_reta = math.sin(val_rad_ops_reta_f)
        sen_ops_reta_f = float('{:.2f}'.format(sen_ops_reta))
        sen_ops_x = math.sin(val_rad_ops_x_f)
        sen_ops_x_f = float('{:.2f}'.format(sen_ops_x))

        # CALCULA O VALOR DE X
        x = (val_reta_adj * sen_ops_x_f) / sen_ops_reta_f

        print('\nx \033[00;36m≅ \033[01;36m{:.2f}'.format(x))