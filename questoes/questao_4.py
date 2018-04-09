## QUESTÃO 4 ##
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos
# a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o
# valor da prestação como sendo o valor da casa a comprar dividido pelo número de
# meses a pagar.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def _get_max_monthly_installment(salary):
    return 0.30*salary


def main():
    house_value = float(input("Type the value of the house: "))
    salary = float(input("Type the salary: "))
    years = float(input("Type the years: "))
    montlhy_installment = house_value / (years * 12)
    max_montlhy_installment = _get_max_monthly_installment(salary)
    if(montlhy_installment > max_montlhy_installment):
        print("Your payment was NOT approved")
    else:
        print("Your payment was approved")


if __name__ == '__main__':
    main()
