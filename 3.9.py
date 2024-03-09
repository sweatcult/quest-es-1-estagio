def converte_para_segundos():
    # solicita a quantidade de dias, horas, minutos e segundos do usuário
    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))
    # converte para segundos
    total_segundos = dias * 24 * 60 * 60 + horas * 60 * 60 + minutos * 60 + segundos
    # imprime o total de segundos
    print(f"O total em segundos é: {total_segundos}s")
# chama a função
converte_para_segundos()
