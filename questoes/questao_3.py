## QUESTÃO 3 ##
# Implementar um programa que calcula o desconto previdenciário de um funcionário.
# O programa deve, dado um salário, retornar o valor do desconto proporcional ao mesmo.
# O cálculo de desconto segue a regra: o desconto deve 11% do valor do salário, entretanto,
# o valor máximo de desconto é 318,20.
# Sendo assim, ou o programa retorna 11% sobre o salário ou 318,20.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

def _get_discount(salary):
    return 0.11*salary


def main():
    salary = float(input("Type your salary: "))
    discount = _get_discount(salary)
    if(discount > 318.20):
        discount = 318.20
    print("You got a discount of", discount, "$")


if __name__ == '__main__':
    main()
