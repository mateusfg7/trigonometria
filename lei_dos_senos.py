import math

class lei_sen:

    def __init__(self):

        print("\n\033[00;36m❰\033[01;36mLEI DOS SENOS\033[00;36m❱\n")

        try:
            valor_reta_adj = float(input('\033[00;36mValor da reta adjacente 》 \033[01;36m'))
            valor_angulo_oposto_reta = float(input('\033[00;36mValor do angulo oposto a reta adjacente 》 \033[01;36m'))
            valor_angulo_oposto_x = float(input('\033[00;36mValor do angulo oposto a X 》 \033[01;36m'))
        except ValueError:
            print("Valores inválidos!")
            exit()


        val_rad_ops_reta = (valor_angulo_oposto_reta / 180) * math.pi # conversão graus para radianos
        val_rad_ops_reta_f = float('{:.2f}'.format(val_rad_ops_reta)) # formatado
        val_rad_ops_x = (valor_angulo_oposto_x / 180) * math.pi # conversão graus para radianos
        val_rad_ops_x_f = float('{:.2f}'.format(val_rad_ops_x)) # formatado
 

        sen_ops_reta = math.sin(val_rad_ops_reta_f)
        sen_ops_reta_f = float('{:.2f}'.format(sen_ops_reta)) # formatado
        sen_ops_x = math.sin(val_rad_ops_x_f)
        sen_ops_x_f = float('{:.2f}'.format(sen_ops_x)) # formatado

        x = (valor_reta_adj * sen_ops_x_f) / sen_ops_reta_f

        print('\nx \033[00;36m≅ \033[01;36m{:.2f}'.format(x))