def calcula_salario_vendedor():
    """Calcula o salário total de um vendedor, considerando salário fixo e comissão sobre as vendas."""

    # Solicita os dados do vendedor
    nome = input("Digite o nome do vendedor: ")
    salario_base = float(input("Digite o salário fixo do vendedor: "))
    total_vendas = float(input("Digite o total de vendas do vendedor: "))

    # Calcula a comissão (15% sobre o total de vendas)
    comissao = total_vendas * 0.15

    # Calcula o salário total
    salario_total = salario_base + comissao

    # Imprime o resultado formatado
    print(f"O salário total de {nome} é R$ {salario_total:.2f}")

# Chama a função principal se o script for executado diretamente
if __name__ == "__main__":
    calcula_salario_vendedor()
