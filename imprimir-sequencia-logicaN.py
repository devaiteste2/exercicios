# Programa em Python para gerar a sequência lógica com N
def imprime_sequencia(n):
    """
    Função que imprime a sequência lógica para o número inteiro N.
    """
    for i in range(1, n + 1):
        # Primeira linha
        print(f"{i} {i**2} {i**3}")
        # Segunda linha
        print(f"{i} {i**2 + 1} {i**3 + 1}")

def main():
    try:
        # Leitura do valor inteiro N
        N = int(input("Digite um valor para N: "))
        
        # Verifica se N está dentro do limite permitido
        if N < 1 or N > 1000:
            raise ValueError("N deve estar entre 1 e 1000")
        
        # Chama a função para imprimir a sequência
        imprime_sequencia(N)
    
    except ValueError as ve:
        print(f"Erro: {ve}")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
