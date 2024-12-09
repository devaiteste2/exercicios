# Programa em Python para calcular o valor total a pagar com base no código e quantidade

def main():
    # Leitura dos valores de código e quantidade
    print("Entre com o valor do código e quantidade")
    codigo, quantidade = map(int, input().split())

    # Dicionário com os preços dos itens baseados no código
    precos = {
        1: 4.00,  # Cachorro Quente
        2: 4.50,  # X-Salada
        3: 5.00,  # X-Bacon
        4: 2.00,  # Torrada simples
        5: 1.50   # Refrigerante
    }

    # Verifica se o código é válido
    if codigo in precos:
        # Calcula o valor total a pagar
        total = precos[codigo] * quantidade

        # Imprime o valor total no formato especificado
        print(f"Total: R$ {total:.2f}")
    else:
        print("Código inválido.")

# Executa a função main() apenas se o script for executado diretamente
if __name__ == "__main__":
    main()
