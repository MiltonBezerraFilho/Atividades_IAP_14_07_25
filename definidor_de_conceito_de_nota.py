nota_1 = float( input("Digite a primeira nota: "))
nota_2 = float( input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

if (media >= 9):
    print("Conceito A")
elif (media >= 7.5):
    print("Conceito B")
elif (media >= 6):
    print("Conceito C")
elif (media >= 4):
    print("Conceito D")
else:
    print("Conceito E")