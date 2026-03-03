from utils_io import obter_inteiro, escrever

def verificar_data(dia, mes, ano):
    if dia < 1 or mes < 1 or mes > 12 or ano < 1:
        return False
    elif mes in (4, 6, 9, 11) and dia > 30:
        return False
    elif mes == 2 and dia > 28:
        return False
    elif dia > 31:
        return False
    return True

def main():
    dia = obter_inteiro('Digite um dia: ')
    mes = obter_inteiro('Digite um mês: ')
    ano = obter_inteiro('Digite um ano: ')

    if verificar_data(dia, mes, ano):
        data = f'A data é válida: {dia}/{mes}/{ano}'
    else:
        data = f'A data é inválida, não existe no calendário Gregoriano'
    escrever(data)
main()
