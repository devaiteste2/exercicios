# Programa em Python para encontrar o maior valor e sua posição entre 100 números

def main():
    maior_valor = None
    posicao_maior = 0

    # Leitura de 100 números inteiros
    for i in range(1, 101):
        valor = int(input())  # Lê o valor inteiro
        
        # Verifica se o valor atual é o maior encontrado até agora
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
            posicao_maior = i  # Armazena a posição do maior valor
    
    # Imprime o maior valor e sua posição
    print(maior_valor)
    print(posicao_maior)

# Executa a função main apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
