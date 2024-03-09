def calcula_desconto():
    # solicita o preço da mercadoria e o percentual de desconto do usuário
    preco = float(input("Digite o preço da mercadoria: "))
    percentual_desconto = float(input("Digite o percentual de desconto: "))
    # calcula o valor do desconto
    valor_desconto = preco * (percentual_desconto / 100)
    # calcula o preço a pagar
    preco_pagar = preco - valor_desconto
    # imprime o valor do desconto e o preço a pagar
    print(f"O valor do desconto é: R${valor_desconto:.2f}")
    print(f"O preço a pagar é: R${preco_pagar:.2f}")
# chama a função
calcula_desconto()
