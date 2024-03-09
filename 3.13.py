def converte_temperatura():
    # solicita a temperatura em graus celsius do usuário
    c = float(input("Digite a temperatura em graus celsius: "))
    # converte a temperatura para graus fahrenheit
    f = 9 * c / 5 + 32
    # imprime a temperatura convertida
    print(f"A temperatura em graus fahrenheit é: {f:.1f}°F")
# chama a função
converte_temperatura()
