## QUESTÃO 6 ##
# Escreva um programa que calcule a porcentagem de nucleotídeos A, C, G e T em
# uma cadeia de DNA informada pelo usuário. Indicar também a quantidade e a
# porcentagem de nucleotídeos inválidos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def _count_nucleotide(dna, letter):
    return len(dna.split(letter)) - 1


def _get_the_percentage(length, letter):
    return (letter / length)*100.0


def main():
    dna = input('Type the dna with all nucleotides together: ')
    A = _count_nucleotide(dna, 'A')
    C = _count_nucleotide(dna, 'C')
    G = _count_nucleotide(dna, 'G')
    T = _count_nucleotide(dna, 'T')
    length = len(dna)
    A_percentage = _get_the_percentage(length, A)
    C_percentage = _get_the_percentage(length, C)
    G_percentage = _get_the_percentage(length, G)
    T_percentage = _get_the_percentage(length, T)
    invalid_percentage = 100 - \
        (A_percentage + C_percentage + G_percentage + T_percentage)

    print("The A percentage is", A_percentage,
          "The C percentage is", C_percentage,
          "The G percentage is", G_percentage,
          "The T percentage is", T_percentage,
          "The invalid percentage is", invalid_percentage)


if __name__ == '__main__':
    main()
