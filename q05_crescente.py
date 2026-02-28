#Leia 3 (três) números e escreva-os em ordem crescente
from utils_io import obter_inteiro

n1 = obter_inteiro('Digite um número: ')
n2 = obter_inteiro('Digite um número: ')
n3 = obter_inteiro('Digite um número: ')

numeros = [n1, n2, n3]

numeros.sort()
print(f'Os números em ordem crescente são: {numeros[0]}, {numeros[1]}, {numeros[2]}')


