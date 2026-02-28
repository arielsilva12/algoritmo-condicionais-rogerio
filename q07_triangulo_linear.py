lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

def eh_triangulo(lado1, lado2, lado3):
    if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado2 + lado3):
        print('Sim, os lados formam um triângulo!')
    else:
        print('Não, os lados não forma um triângulo!')
    
def obter_tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        print('E o triângulo é do tipo Equilátero')
    elif lado1 != 2 and lado1 != lado3 and lado2 != lado3:
        print('E o triângulo é do tipo Escaleno')
    else:
        print('E o triângulo é do tipo Isósceles')

eh_triangulo(lado1, lado2, lado3)
obter_tipo_triangulo(lado1, lado2, lado3)