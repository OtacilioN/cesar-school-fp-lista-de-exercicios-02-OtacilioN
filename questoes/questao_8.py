## QUESTÃO 8 ##
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data
# será inserida em formato numérico com três instruções de entrada separadas;
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

from constants_8 import *


def _is_multiple(number, multiple):
    return not bool(number % multiple)


def _is_leap(year):
    if _is_multiple(year, 400) or (_is_multiple(year, 4) and not _is_multiple(year, 100)):
        return 1
    return 0


def _is_31_month(month):
    if (month in MONTHS_WITH_31_DAYS):
        return 1
    return 0


def main():
    # User inputs
    year = int(input("Type the year: "))
    month = int(input("Type the month: "))
    day = int(input("Type the day: "))

    if month == FEBRUARY:
        if day < FEBRUARY_MAX + _is_leap(year):
            day += 1
        else:
            day = 0
            month += 1
    else:
        if day < MONTH_30 + _is_31_month(month):
            day += 1
        else:
            day = 0
            if month == DECEMBER:
                month = 0
                year += 1
            else:
                month += 1

    print(str(year)+"-"+str(month)+"-"+str(day))


if __name__ == '__main__':
    main()
