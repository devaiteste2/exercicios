# Programa em Python para calcular o tempo que a população de A levará para ultrapassar B
def calcular_anos(PA, PB, G1, G2):
    """
    Função que calcula quantos anos a população de A leva para ultrapassar B.
    Se ultrapassar 100 anos, retorna "Mais de 1 século".
    :param PA: População inicial de A.
    :param PB: População inicial de B.
    :param G1: Taxa de crescimento anual (%) da população de A.
    :param G2: Taxa de crescimento anual (%) da população de B.
    :return: Número de anos ou a mensagem "Mais de 1 século".
    """
    anos = 0
    while PA <= PB:
        # Incremento das populações considerando as taxas de crescimento
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1
        
        # Limite de 100 anos
        if anos > 100:
            return "Mais de 1 século"
    
    return anos

def main():
    """
    Função principal para ler os dados e calcular os resultados.
    """
    try:
        # Leitura do número de casos de teste
        T = int(input("Digite o número de casos de teste: "))
        
        # Loop pelos casos de teste
        for _ in range(T):
            # Leitura de PA, PB, G1, G2
            valores = input("Digite PA, PB, G1, G2: ").split()
            PA, PB = int(valores[0]), int(valores[1])
            G1, G2 = float(valores[2]), float(valores[3])
            
            # Chama a função para calcular o número de anos
            resultado = calcular_anos(PA, PB, G1, G2)
            
            # Imprime o resultado
            print(resultado)
    
    except ValueError as ve:
        print(f"Erro: {ve}")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
