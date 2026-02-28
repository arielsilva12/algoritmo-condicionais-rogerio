#Leia 3 (três) números e escreva-os em ordem crescente
from utils_lista import ler_tres_inteiros

n1, n2, n3 = ler_tres_inteiros()

numeros = [n1, n2, n3]

numeros.sort()
print(f'Os números em ordem crescente são: {numeros[0]}, {numeros[1]}, {numeros[2]}')


