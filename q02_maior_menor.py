#Ler dois números, verificar e escrever o maior e o menor entre os números lidos
from utils_lista import ler_dois_inteiros

numero1, numero2 = ler_dois_inteiros()

maior = max(numero1, numero2)
menor = min(numero1, numero2)

if numero1 == numero2:
    print ('Os números são iguais!')
else:
    print(f'O menor número é o {menor} e o maior número é o {maior}')
    