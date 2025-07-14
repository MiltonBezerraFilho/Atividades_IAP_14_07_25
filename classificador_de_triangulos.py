lado_1 = float( input("Digite o valor do primero lado do triângulo: "))
lado_2 = float( input("Digite o segundo valor: "))
lado_3 = float( input("Digite o terceiro valor "))

if (lado_1 == lado_2 == lado_3):
    print("É um triangulo equilátero.")
elif (lado_1 == lado_2 != lado_3 or lado_1 != lado_2 == lado_3 or lado_3 == lado_1 != lado_2):
    print("É um triângulo isóceles.")
else:
    print("É um triângulo escaleno.")