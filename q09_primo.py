from utils_io import obter_inteiro, escrever

def verificar_primo(numero):
    if numero <= 1:
        return False
    elif numero in (2, 3, 5, 7):
        return True
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        return False
    return True

def main():
    numero = obter_inteiro('Digite um número para verificar se é primo: ')

    if verificar_primo(numero):
        resultado = f'O número {numero} é um número primo!'
    else:
        resultado = f'O número {numero} não é primo'

    escrever(resultado)
main()