#Ler dois números, verificar e escrever o maior e o menor entre os números lidos
from utils_io import obter_inteiro

numero1 = obter_inteiro('Digite um número: ')
numero2 = obter_inteiro('Digite mais esse número: ')

maior = max(numero1, numero2)
menor = min(numero1, numero2)

if numero1 == numero2:
    print ('Os números são iguais!')
else:
    print(f'O menor número é o {menor} e o maior número é o {maior}')
    