# Programa em Python para calcular o novo salário com reajuste
def calcular_reajuste(salario):
    """
    Função que calcula o novo salário, o reajuste ganho e o percentual de acordo com a faixa salarial.
    :param salario: Salário atual.
    :return: Uma tupla contendo o novo salário, o reajuste ganho e o percentual.
    """
    if salario <= 400.00:
        percentual = 15
    elif salario <= 800.00:
        percentual = 12
    elif salario <= 1200.00:
        percentual = 10
    elif salario <= 2000.00:
        percentual = 7
    else:
        percentual = 4

    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
    return novo_salario, reajuste, percentual

def main():
    """
    Função principal para calcular e exibir o novo salário com reajuste.
    """
    try:
        # Leitura do valor do salário
        salario = float(input("Digite o salário atual: "))
        
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        
        # Chama a função para calcular o novo salário, reajuste e percentual
        novo_salario, reajuste, percentual = calcular_reajuste(salario)
        
        # Imprime os resultados no formato solicitado
        print(f"Novo salário: R$ {novo_salario:.2f}")
        print(f"Reajuste ganho: R$ {reajuste:.2f}")
        print(f"Percentual: {percentual} %")
    
    except ValueError as ve:
        print("Por favor, insira um valor válido para o salário.")
        print(f"Erro: {ve}")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()

