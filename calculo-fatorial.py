# Programa Python para calcular o fatorial de um número
def calcular_fatorial(n):
    """
    Função que calcula o fatorial de um número inteiro.
    :param n: Número inteiro positivo.
    :return: O fatorial de n.
    """
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

def main():
    """
    Função principal para ler um número, validar e calcular o fatorial.
    """
    try:
        # Leitura do valor inteiro
        N = int(input("Digite um número inteiro entre 1 e 20: "))
        
        # Verifica se está dentro do limite permitido
        if N < 1 or N > 20:
            raise ValueError("O número deve estar entre 1 e 20.")
        
        # Chama a função para calcular o fatorial
        resultado = calcular_fatorial(N)
        
        # Imprime o resultado
        print(f"O fatorial de {N} é: {resultado}")
    
    except ValueError as ve:
        print(f"Erro: {ve}")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
