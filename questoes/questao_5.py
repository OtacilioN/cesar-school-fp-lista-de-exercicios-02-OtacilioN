## QUESTÃO 5 ##
# Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é
# Equilátero, Isósceles ou Escaleno.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!!
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##

def main():
    triangle_sides = [float(side) for(side) in input(
        "Type the sizes of each side spaced between: ").split()]

    if(triangle_sides[0] == triangle_sides[1]):
        if(triangle_sides[1] == triangle_sides[2]):
            print("Your triangle is Equilateral")
            return
    elif(triangle_sides[0] != triangle_sides[2]):
        if(triangle_sides[1] != triangle_sides[2]):
            print("Your triangle is Scalene")
            return

    print("Your triangle is Isosceles")


if __name__ == '__main__':
    main()
