# Programa em Python para calcular a soma de números ímpares entre X e Y

def main():
    try:
        # Leitura do número de casos de teste
        N = int(input("Digite o número de casos de teste: "))
        
        # Verifica se N está dentro do limite permitido
        if N < 1:
            raise ValueError("O número de casos de teste (N) deve ser maior que zero.")
        
        # Loop para cada caso de teste
        for _ in range(N):
            # Leitura dos valores X e Y
            X, Y = map(int, input("Digite os valores de X e Y separados por espaço: ").split())
            
            # Define os limites corretos (menor e maior)
            if X > Y:
                X, Y = Y, X
            
            # Calcula a soma dos números ímpares entre X e Y, excluindo os limites
            soma = sum(i for i in range(X + 1, Y) if i % 2 != 0)
            
            # Imprime o resultado da soma
            print(soma)
    
    except ValueError as ve:
        print(f"Erro: {ve}")

# Executa a função main apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
