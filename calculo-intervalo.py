# Programa em Python para verificar em qual intervalo o valor se encontra

def main():
    # Leitura do valor de ponto flutuante
    print("entre com o valor")
    valor = float(input())

    # Verifica em qual intervalo o valor se encontra
    if 0 <= valor <= 25:
        print("Intervalo [0,25]")
    elif 25 < valor <= 50:
        print("Intervalo (25,50]")
    elif 50 < valor <= 75:
        print("Intervalo (50,75]")
    elif 75 < valor <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
