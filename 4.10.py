def calcula_tipo():
    # solicita o tipo e o consumo de kwh 
    tipo = input("Digite o tipo de instalaçao(R, C ou I): ").upper()
    kwh = float(input("Digite a kwh consumida: "))
    # verifica o tipo e o kwh
    if tipo == "R":
        valor_pagar = kwh * 0.40 if kwh <= 500 else kwh * 0.65
    elif tipo == "C":
        valor_pagar = kwh * 0.55 if kwh <= 1000 else kwh * 0.60
    elif tipo == "I":
        valor_pagar = kwh * 0.55 if kwh <= 5000 else kwh * 0.60
    # mensagem de erro caso não seja R, C ou I
    else:
        print("Tipo de instalação não existe")
    # imprime o valor a pagar
    if valor_pagar:
        print(f"O valor pago é de R$: {valor_pagar:.2f}")
# chama a função    
calcula_tipo()
    
