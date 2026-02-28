#Ler três números, verificar e escrever quantos números iguais existem entre os números
from utils_lista import ler_tres_inteiros

numero1, numero2, numero3 = ler_tres_inteiros()

if numero1 == numero2 == numero3:
    print('Os 3 números são iguais!')
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print('2 dos 3 números são iguais!')
else:
    print('Todos os números são diferentes')