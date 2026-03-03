from utils_io import obter_inteiro

def calcular_dezena_unidade(numero):
    dezena = numero // 10
    unidade = numero % 10
    if dezena == unidade:
        print(f"O algarismo da dezena {dezena} é igual ao algarismo da unidade {unidade}")
    else:
        print(f'O algarismo da dezena {dezena} é diferente do algarismo da unidade {unidade}')

def main():
    numero = obter_inteiro('Digite um número de 2 dígitos: ')

    calcular_dezena_unidade(numero)
main()