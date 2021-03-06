import math
import sys

try:
    try:
        calc = sys.argv[1]
        valor_um = float(sys.argv[2])
        valor_dois = float(sys.argv[3])
        valor_tres = float(sys.argv[4])
    except ValueError:
        print("valor inválido!")
        exit()


    def lei_cos(val_um, val_dois, val_angulo):

        val_um_quad = math.pow(val_um,2)
        val_dois_quad = math.pow(val_dois,2)
        val_angulo_rad = (val_angulo / 180) * math.pi
        cos_angulo = float('{:.2f}'.format(math.cos(val_angulo_rad)))
        x = math.sqrt(val_um_quad + val_dois_quad - 2 * val_um * val_dois * cos_angulo)

        print('x ≅ {:.2f}'.format(x))


    def lei_sen(val_reta_adj, val_ang_ops_reta, val_ang_ops_x):
        
        val_rad_ops_reta = float('{:.2f}'.format((val_ang_ops_reta / 180) * math.pi))
        val_rad_ops_x = float('{:.2f}'.format((val_ang_ops_x / 180) * math.pi))
        sen_ops_reta = float('{:.2f}'.format(math.sin(val_rad_ops_reta)))
        sen_ops_x = float('{:.2f}'.format(math.sin(val_rad_ops_x)))
        x = (val_reta_adj * sen_ops_x) / sen_ops_reta

        print('x ≅ {:.2f}'.format(x))

    
    def area_tri(reta_a, reta_b, angulo):

        angulo_rad = float('{:.2f}'.format((angulo / 180) * math.pi))
        sen_angulo = float('{:.2f}'.format(math.sin(angulo_rad)))
        area = (reta_a * reta_b * sen_angulo) / 2

        print('área = {}'.format(area))


    if calc == "leiCos":
        lei_cos(valor_um, valor_dois, valor_tres)
    elif calc == "leiSen":
        lei_sen(valor_um, valor_dois, valor_tres)
    elif calc == "areaTri":
        area_tri(valor_um, valor_dois, valor_tres)


except IndexError:
    print("\nUse trig-otm.py [calculo] [valor 1] [valor 2] [valor 3]")
    print("\nCalculos disponíveis:")
    print(" \nleiCos - calcula usando a lei dos cossenos")
    print("   valor 1 = reta adjacente 1")
    print("   valor 2 = reta adjacente 2")
    print("   valor 3 = ângulo")
    print(" \nleiSen - calcula usando a lei dos senos")
    print("   valor 1 = reta adjacente")
    print("   valor 2 = ângulo oposto a reta adjacente")
    print("   valor 3 = ângulo oposto a X")
    print(" \nareaTri - calcula a área do triângulo")
    print("   valor 1 = reta a")
    print("   valor 2 = reta b")
    print("   valor 3 = ângulo")