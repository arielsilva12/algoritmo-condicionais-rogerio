from utils_io import obter_inteiro
from utils_geometria import verificar_triangulo_angulo, classificar_triangulo_angulo

def main():
    angulo1 = obter_inteiro('Ângulo 1: ')
    angulo2 = obter_inteiro('Ângulo 2: ')
    angulo3 = obter_inteiro('Ângulo 3: ')

    if verificar_triangulo_angulo(angulo1, angulo2, angulo3):
        print('Sim, esses ângulos formam um triângulo!')
        tipo = classificar_triangulo_angulo(angulo1, angulo2, angulo3)
        print(f'E o tipo do triângulo é do tipo {tipo}')
    else:
        print('Não é um triângulo, pois a soma não é 180°.')
    
if __name__ == "__main__":
    main()


    

