# Programa em Python para validar duas notas e calcular a média semestral
def validar_nota(nota):
    """
    Função que valida se a nota está no intervalo [0, 10].
    :param nota: Valor da nota a ser validada.
    :return: True se a nota for válida, False caso contrário.
    """
    if 0 <= nota <= 10:
        return True
    else:
        print("Nota inválida.")
        return False

def calcular_media():
    """
    Função que lê duas notas válidas e calcula a média semestral.
    """
    notas_validas = []
    while len(notas_validas) < 2:
        try:
            # Leitura da nota
            nota = float(input("Digite uma nota entre 0 e 10: "))
            
            # Validação da nota
            if validar_nota(nota):
                notas_validas.append(nota)
        except ValueError:
            print("Valor inválido. Por favor, insira um número.")

    # Calcula e imprime a média semestral
    media = sum(notas_validas) / 2
    print(f"Média semestral: {media:.2f}")

def main():
    """
    Função principal para executar o cálculo da média.
    """
    calcular_media()

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
