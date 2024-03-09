def calcula_aumento():
    # solicita o valor do salário e a porcentagem de aumento do usuário
    salario = float(input("Digite o valor do salário: "))
    porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))
    # calcula o valor do aumento
    valor_aumento = salario * (porcentagem_aumento / 100)
    # calcula o novo salário
    novo_salario = salario + valor_aumento
    # imprime o valor do aumento e o novo salário
    print(f"O valor do aumento é: R${valor_aumento:.2f}")
    print(f"O novo salário é: R${novo_salario:.2f}")
# chama a função
calcula_aumento()
