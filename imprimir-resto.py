# Programa em Python para imprimir todos os valores entre X e Y cujo resto por 5 seja 2 ou 3

def main():
    try:
        # Leitura dos valores X e Y
        X = int(input("Digite o valor de X: "))
        Y = int(input("Digite o valor de Y: "))

        # Define os limites corretos (menor e maior)
        if X > Y:
            X, Y = Y, X

        # Loop para verificar cada valor entre X e Y (excluindo X e Y)
        for i in range(X + 1, Y):
            # Verifica se o resto da divisão por 5 é 2 ou 3
            if i % 5 == 2 or i % 5 == 3:
                print(i)

    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números inteiros.")

# Executa a função main apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
