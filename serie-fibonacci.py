# Programa Python para gerar a série de Fibonacci até o N-ésimo termo
def fibonacci(n):
    """
    Função que gera a série de Fibonacci até o N-ésimo termo.
    """
    # Inicializa os dois primeiros valores da série
    a, b = 0, 1
    resultado = [a]
    
    # Gera os termos da série de Fibonacci
    for i in range(1, n):
        resultado.append(b)
        a, b = b, a + b
    
    return resultado

def main():
    try:
        # Leitura do valor inteiro N
        N = int(input("Digite um valor inteiro para N: "))
        
        # Verifica se está dentro do limite permitido
        if N < 1 or N > 46:
            raise ValueError("O valor de N deve estar entre 1 e 46")
        
        # Chama a função para gerar a série de Fibonacci e armazena a sequência
        sequencia = fibonacci(N)
        
        # Imprime a sequência gerada
        print("Série de Fibonacci:", sequencia)
    
    except ValueError as ve:
        print(f"Erro: {ve}")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
