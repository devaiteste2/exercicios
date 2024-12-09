def calcular_valor_total_pecas():
    """Calcula o valor total a ser pago por duas peças, considerando a quantidade e o valor unitário de cada uma."""

    # Lê os dados da primeira peça
    codigo_peca1, quantidade_peca1, valor_unitario_peca1 = input("Digite o código, quantidade e valor unitário da primeira peça (separados por espaço): ").split()
    codigo_peca1 = int(codigo_peca1)
    quantidade_peca1 = int(quantidade_peca1)
    valor_unitario_peca1 = float(valor_unitario_peca1)

    # Lê os dados da segunda peça
    codigo_peca2, quantidade_peca2, valor_unitario_peca2 = input("Digite o código, quantidade e valor unitário da segunda peça (separados por espaço): ").split()
    codigo_peca2 = int(codigo_peca2)
    quantidade_peca2 = int(quantidade_peca2)
    valor_unitario_peca2 = float(valor_unitario_peca2)

    # Calcula o valor total a ser pago
    valor_total = (quantidade_peca1 * valor_unitario_peca1) + (quantidade_peca2 * valor_unitario_peca2)

    # Imprime o valor total formatado
    print(f"VALOR A PAGAR: R$ {valor_total:.2f}")

# Chama a função principal se o script for executado diretamente
if __name__ == "__main__":
    calcular_valor_total_pecas()
