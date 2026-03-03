from utils_io import obter_inteiro

def calcular_maior(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'O número {num1} é maior')
    elif num2 > num1 and num2 > num3:
        print(f'O número {num2} é maior')
    elif num3 > num1 and num3 > num2:
        print(f'O número {num3} é maior')

def main():
    num1 = obter_inteiro('Digite um núumero: ')
    num2 = obter_inteiro('Digite um número: ')
    num3 = obter_inteiro('Digite só mais esse número: ')

    calcular_maior(num1, num2, num3)
main()

#maior = max(num1, num2, num3) pegar o maior número
