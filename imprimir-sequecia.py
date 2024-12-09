# Programa em Python para imprimir a sequência IJ conforme o exemplo fornecido

def main():
    # Inicializa os valores de I e J
    I = 1
    J = 60

    # Loop que continua enquanto J for maior ou igual a zero
    while J >= 0:
        # Imprime a saída no formato especificado
        print(f"I={I} J={J}")
        
        # Incrementa I em 3 e decrementa J em 5
        I += 3
        J -= 5

# Executa a função main apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
