## QUESTÃO 1 ##
# Faça um programa que receba cinco inteiros e diga qual deles é o maior e qual o menor.
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

# Used bubble sort to not overkill with quick sort, making the code cleaner instead optimized
# It works for N numbers instead 5


def sort(myNumbers):
    for actualNumber in range(len(myNumbers)-1, 0, -1):
        for i in range(actualNumber):
            if myNumbers[i] > myNumbers[i+1]:
                temp = myNumbers[i]
                myNumbers[i] = myNumbers[i+1]
                myNumbers[i+1] = temp


def main():
    myNumbers = [int(number) for number in input(
        'Type the five numbers spaced between(Such as: 5 4 3 2 1): ').split()]
    sort(myNumbers)

    # Printing the first element in the sorted array
    print(myNumbers[0])


if __name__ == '__main__':
    main()
