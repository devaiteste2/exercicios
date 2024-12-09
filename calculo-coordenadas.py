def main():
    # Entrada de coordenadas para o primeiro ponto
    print("ENtre com os valores")
    x1, y1 = map(float, input().split())
    # Entrada de coordenadas para o segundo ponto
    print("segundo valor")
    x2, y2 = map(float, input().split())

    # Cálculo da distância euclidiana
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Impressão da distância formatada com 4 casas decimais
    print(f"A distância calculada é: {distancia:.4f}")


# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
