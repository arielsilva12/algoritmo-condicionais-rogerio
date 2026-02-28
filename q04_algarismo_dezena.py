numero = int(input('Digite um número de 2 dígitos: '))

dezena = numero // 10
unidade = numero % 10

if dezena == unidade:
    print("O algarismo da dezena é igual ao algarismo da unidade: ")
else:
    print('O algarismo da dezena é diferente do algarismo da unidade: ')
