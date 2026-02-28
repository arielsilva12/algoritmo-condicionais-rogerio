from utils_io import obter_inteiro

num1 = obter_inteiro('Digite um núumero: ')
num2 = obter_inteiro('Digite um número: ')
num3 = obter_inteiro('Dogote só mais esse número: ')

maior = max(num1, num2, num3) #pegar o maior número

print(f'O maior número é o {maior}')
