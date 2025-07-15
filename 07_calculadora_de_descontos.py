valor = float( input("Digite o valor: "))
formato = str( input("Digite a forma de pagamento: "))

if (formato == "Cartão" or formato == "cartão"):
    print("Formato de pagamento inválido.")
elif (formato == "Cheque" or formato == "cheque"):
    print(f'O preço é R${valor}')
elif (formato == "Dinheiro" or formato == "dinheiro"):
    if (valor <= 99.9):
        print(f'O preço é R$ {valor}')
    else:
        print(f'O preço é R$ {valor - (valor * 0.1)}')