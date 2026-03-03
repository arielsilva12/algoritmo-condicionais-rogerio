from utils_io import obter_inteiro, escrever

def calcular_idade(dia_atual, mes_atual, ano_atual, dia_nsc, mes_nsc, ano_nsc):
    idade = ano_atual - ano_nsc

    if mes_atual < mes_nsc:
        idade -= 1
    elif mes_atual == mes_nsc and dia_atual < dia_nsc:
        idade -= 1
   
    return idade

def main():
    dia_atual = obter_inteiro('Digite o dia atual: ')
    mes_atual = obter_inteiro('Digite o mês atual: ')
    ano_atual = obter_inteiro('Digite o ano atual: ')

    dia_nsc = obter_inteiro('Digite o seu dia de nascimento: ')
    mes_nsc = obter_inteiro('Digite o mês em que você nasceu:  ')
    ano_nsc = obter_inteiro('Digite o ano em que você nasceu: ')

    resultado = calcular_idade(dia_atual, mes_atual, ano_atual, dia_nsc, mes_nsc, ano_nsc)
    escrever(f'Você tem {resultado} anos de idade!')

main()  

