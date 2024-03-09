def calcula_tempo_viagem():
    # solicita a distância e a velocidade média
    distancia = float(input("Digite a distância a percorrer (em km): "))
    velocidade_media = float(input("Digite a velocidade média esperada para a viagem (em km/h): "))
    # calcula o tempo da viagem
    tempo = distancia / velocidade_media
    # converte as horas em minutos
    horas = int(tempo)
    minutos = (tempo - horas) * 60
    # imprime o tempo da viagem
    print(f"O tempo estimado da viagem é: {horas} horas e {minutos:.0f} minutos")
# chama a função
calcula_tempo_viagem()
