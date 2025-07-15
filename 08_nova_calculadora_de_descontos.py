valor = float( input("Digite o valor: "))
formato = str( input("Digite a forma de pagamento: "))

if (formato == "Cheque" or formato == "cheque"):
    print(f'O preço é R${valor}')
elif (formato == "Dinheiro" or formato == "dinheiro"):
    if (valor <= 99.9):
        print(f'O preço é R$ {valor}')
    else:
        print(f'O preço é R$ {valor - (valor * 0.1)}')
elif (formato == "Cartão" or formato == "cartão"):
    funcao = str( input("Crédito ou débito: "))
if (funcao == "Débito" or funcao == "débito"):
    print(f'O preço é R$ {valor}')
elif (funcao == "Crédito" or funcao == "crédito"):
    parcelas = int( input("Digite o número de parcelas (Até 3 vezes): "))
if (parcelas > 3 or parcelas < 1):
    print("Número inválido de parcelas.")
else:
    print(f'O preço é R$ {valor} em {parcelas} parcelas de R$ {valor / parcelas}')