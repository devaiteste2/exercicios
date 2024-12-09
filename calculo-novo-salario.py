def main():
    # Leitura do salário atual do funcionário
    print("Digite o valor do salario")
    salario_atual = float(input())

    # Definição dos reajustes de acordo com a faixa salarial
    if salario_atual <= 400.00:
        percentual = 15
    elif salario_atual <= 800.00:
        percentual = 12
    elif salario_atual <= 1200.00:
        percentual = 10
    elif salario_atual <= 2000.00:
        percentual = 7
    else:
        percentual = 4

    # Calcula o reajuste e o novo salário
    reajuste = salario_atual * (percentual / 100)
    novo_salario = salario_atual + reajuste

    # Imprime os resultados no formato especificado
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()

