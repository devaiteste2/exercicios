# Programa em Python para realizar a divisão entre X e Y, tratando erro de divisão por zero

def main():
    try:
        # Leitura do número de pares de valores (N)
        N = int(input("Digite o número de pares de valores: "))
        
        # Verifica se N está dentro do limite permitido
        if N < 1:
            raise ValueError("O número de pares de valores (N) deve ser maior que zero.")
        
        # Loop para cada caso de divisão
        for _ in range(N):
            try:
                # Leitura dos valores X e Y
                X, Y = map(int, input("Digite os valores de X e Y separados por espaço: ").split())
                
                # Verifica se a divisão é possível (evita divisão por zero)
                if Y == 0:
                    print("divisao impossivel")
                else:
                    # Realiza a divisão e imprime o resultado com 1 casa decimal
                    resultado = X / Y
                    print(f"{resultado:.1f}")
            except ValueError:
                print("Erro: Certifique-se de inserir dois números inteiros separados por espaço.")
    
    except ValueError as ve:
        print(f"Erro: {ve}")

# Executa a função main apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
