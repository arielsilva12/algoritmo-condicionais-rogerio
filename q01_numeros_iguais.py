#Ler três números, verificar e escrever quantos números iguais existem entre os números
from utils_io import obter_inteiro

numero1 = obter_inteiro('Digite um número: ')
numero2 = obter_inteiro('Digite outro número: ')
numero3 = obter_inteiro('Digite só mais esse número: ')

if numero1 == numero2 == numero3:
    print('Os 3 números são iguais!')
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print('2 dos 3 números são iguais!')
else:
    print('Todos os números são diferentes')