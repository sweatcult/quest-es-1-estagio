def calcula_distancia():
    # solicita ao usuário a distância desejada
    distancia = float(input("Digite a distância em km: "))
    # definição dos preços em km
    passagem_menor = 0.50
    passagem_maior = 0.45
    # verifica se a distância é maior ou igual a 200 km
    if distancia > 200:
        preco_passagem = passagem_maior * distancia
    elif distancia <= 200:
        preco_passagem = passagem_menor * distancia
    # imprime o preço da passagem
    print(f"{preco_passagem:.2f}")
# chama a função 
calcula_distancia()
