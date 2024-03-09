def calcula_reducao():
    # solicita a quantidade de cigarros fumados por dia e a quantidade de anos que o usuário fumou
    cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
    anos_fumando = int(input("Digite a quantidade de anos que fumou: "))
    # calcula a quantidade total de cigarros fumados
    total_cigarros = cigarros_por_dia * anos_fumando * 365
    # calcula a quantidade de dias de vida perdidos (10 minutos por cigarro, convertido para dias)
    dias_perdidos = (total_cigarros * 10) / (60 * 24)
    # imprime a quantidade de dias de vida perdidos
    print(f"O fumante perdeu {dias_perdidos:.0f} dias de vida devido ao fumo.")
# chama a função
calcula_reducao()
