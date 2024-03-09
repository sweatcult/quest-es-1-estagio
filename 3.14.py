def calcula_aluguel():
    # solicita a quantidade de km percorridos e a quantidade de dias do aluguel
    km_percorridos = float(input("Digite a quantidade de km percorridos: "))
    dias_aluguel = int(input("Digite a quantidade de dias do aluguel: "))
    # calcula o preço do aluguel
    preco_aluguel = dias_aluguel * 60 + km_percorridos * 0.15
    # imprime o preço a pagar
    print(f"O preço a pagar é: R${preco_aluguel:.2f}")
# chama a função
calcula_aluguel()
