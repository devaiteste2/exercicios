# Programa em Python para determinar o quadrante de um ponto cartesiano
def determinar_quadrante(x, y):
    """
    Função que determina o quadrante de um ponto (x, y).
    :param x: Coordenada x do ponto.
    :param y: Coordenada y do ponto.
    :return: String indicando o quadrante ou a posição do ponto.
    """
    if x == 0 or y == 0:
        return "ponto sobre um dos eixos"
    elif x > 0 and y > 0:
        return "primeiro quadrante"
    elif x < 0 and y > 0:
        return "segundo quadrante"
    elif x < 0 and y < 0:
        return "terceiro quadrante"
    elif x > 0 and y < 0:
        return "quarto quadrante"

def main():
    """
    Função principal para ler as coordenadas e determinar o quadrante.
    """
    while True:
        try:
            # Leitura das coordenadas X e Y
            x, y = map(int, input("Digite as coordenadas X e Y (separadas por espaço): ").split())
            
            # Verifica se uma das coordenadas é zero para encerrar o programa
            if x == 0 or y == 0:
                break
            
            # Chama a função para determinar o quadrante e imprime o resultado
            print(determinar_quadrante(x, y))
        
        except ValueError:
            print("Por favor, insira dois valores inteiros.")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
