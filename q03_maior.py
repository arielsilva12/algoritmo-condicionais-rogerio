from utils_lista import ler_tres_inteiros

num1, num2, num3 = ler_tres_inteiros() #entrada, com uma função que criei no utils_lista
maior = max(num1, num2, num3) #pegar o maior número

print(f'O maior número é o {maior}')
