# Programa em Python para imprimir uma sequência de 1 até Y, quebrando em blocos de X números
def imprimir_sequencia(X, Y):
    """
    Função que imprime a sequência de 1 até Y, quebrando a linha a cada X números.
    :param X: Quantidade de números por linha.
    :param Y: Último número da sequência.
    """
    for i in range(1, Y + 1):
        # Imprime o número sem nova linha no final
        print(i, end=" ")
        
        # A cada X números, quebra a linha
        if i % X == 0:
            print()  # Quebra a linha após X números
    
    # Se Y não for múltiplo de X, imprime a última linha sem quebra
    if Y % X != 0:
        print()

def main():
    """
    Função principal para ler os valores de X e Y e chamar a função para imprimir a sequência.
    """
    try:
        # Leitura dos valores de X e Y
        X, Y = map(int, input("Digite os valores de X e Y (separados por espaço): ").split())
        
        # Chama a função para imprimir a sequência
        imprimir_sequencia(X, Y)
    
    except ValueError:
        print("Erro: Por favor, insira dois valores inteiros válidos.")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
