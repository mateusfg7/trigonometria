import math

class area_tri:

    def __init__(self):

        print("\n\033[00;36m❰\033[01;36mÁREA DE UM TRIÂNGULO\033[00;36m❱\n")

        try:
            reta_a = float(input('\033[00;36mReta a 》 \033[01;36m'))
            reta_b = float(input('\033[00;36mReta b 》 \033[01;36m'))
            angulo = float(input('\033[00;36mÂngulo 》 \033[01;36m'))
        except ValueError:
            print("Valores inválidos!")
            exit()

        angulo_rad = (angulo / 180) * math.pi # conversão graus para radianos

        sen_angulo = math.sin(angulo_rad)
        sen_angulo_f = float('{:.2f}'.format(sen_angulo)) # formatado


        area = (reta_a * reta_b * sen_angulo_f) / 2

        print('\nA \033[00;36m= \033[01;36m{:.2f}'.format(area))