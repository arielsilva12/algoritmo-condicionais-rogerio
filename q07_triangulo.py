from utils_io import obter_inteiro
from utils_geometria import verificar_triangulo_lado, classificar_triangulo_lado

def main():
    lado1 = obter_inteiro('Lado 1: ')
    lado2 = obter_inteiro('Lado 2: ')
    lado3 = obter_inteiro('Lado 3: ')

    if verificar_triangulo_lado(lado1, lado2, lado3):
        print('Sim, os lados forma um triângulo!')
        tipo = classificar_triangulo_lado(lado1, lado2, lado3)
        print(f'E o tipo do triângulo é {tipo}')
    else:
        print('Não, os lados não formam um triângulo!')
if __name__ == "__main__":
    main()
