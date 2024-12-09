# Programa em Python para validar os valores conforme as condições fornecidas

def main():
    # Leitura dos valores inteiros A, B, C e D
    print("Entre com os valores")
    A, B, C, D = map(int, input().split())

    # Verifica todas as condições para os valores serem aceitos
    if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
