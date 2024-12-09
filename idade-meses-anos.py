# Programa em Python para calcular a idade em anos, meses e dias
def calcular_idade_em_dias(dias):
    """
    Função que calcula a idade em anos, meses e dias a partir de um valor em dias.
    :param dias: Número inteiro representando a idade em dias.
    :return: Uma tupla contendo (anos, meses, dias restantes).
    """
    anos = dias // 365  # Calcula o número de anos
    dias_restantes = dias % 365  # Dias restantes após calcular os anos
    meses = dias_restantes // 30  # Calcula o número de meses
    dias_restantes = dias_restantes % 30  # Dias restantes após calcular os meses
    return anos, meses, dias_restantes

def main():
    """
    Função principal para ler o número de dias e calcular a idade em anos, meses e dias.
    """
    try:
        # Leitura do valor inteiro que representa a idade em dias
        dias = int(input("Digite o número de dias para calcular a idade: "))
        
        if dias < 0:
            raise ValueError("O número de dias não pode ser negativo.")
        
        # Chama a função para calcular a idade
        anos, meses, dias_restantes = calcular_idade_em_dias(dias)
        
        # Imprime a saída no formato solicitado
        print(f"{anos} ano(s)")
        print(f"{meses} mes(es)")
        print(f"{dias_restantes} dia(s)")
    
    except ValueError as ve:
        print("Por favor, insira um valor inteiro válido.")
        print(f"Erro: {ve}")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
