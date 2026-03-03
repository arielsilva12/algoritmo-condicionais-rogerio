#Leia 3 (três) números e escreva-os em ordem crescente
from utils_io import obter_inteiro

def ordenar_crescente(n1, n2, n3):
    if n1 > n2 > n3:
        print(f'A ordem crescente é: {n3}, {n2}, {n1}')
    elif n1 > n3 > n2:
        print(f'A ordem crescente é: {n2}, {n3}, {n1}')
    elif n2 > n1 > n3:
        print(f'A ordem crescente é: {n3}, {n1}, {n2}')
    elif n2 > n3 > n1:
        print(f'A ordem crescente é: {n1}, {n3}, {n2}')
    elif n3 > n2 > n1:
        print(f'A ordem crescente é: {n1}, {n2}, {n3}')
    elif n3 > n1 > n2:
        print(f'A ordem crescente é: {n2}, {n1}, {n3}')

def main():
    n1 = obter_inteiro('Digite um número: ')
    n2 = obter_inteiro('Digite um número: ')
    n3 = obter_inteiro('Digite um número: ')

    ordenar_crescente(n1, n2, n3)
main()



#def ordenar_crescente(n1, n2, n3):
    #numeros = [n1, n2, n3]

    #numeros.sort()
    #print(f'Os números em ordem crescente são: {numeros[0]}, {numeros[1]}, {numeros[2]}')
#main()


