entrada = str( input("Digite o seu horário \n(M para matutino, V para vespertino e N para noturno): "))

if (entrada == "M") or (entrada == "m"):
    print("Bom dia!")
elif (entrada == "V") or (entrada == "v"):
    print("Boa tarde!")
elif (entrada == "N") or (entrada == "n"):
    print("Boa noite!")
else:
    print("Valor inválido!")