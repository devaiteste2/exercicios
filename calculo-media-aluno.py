# Programa em Python para calcular a média de um aluno e verificar sua situação

def main():
    # Leitura das notas N1, N2, N3 e N4
    N1, N2, N3, N4 = map(float, input("Digite as notas N1, N2, N3 e N4 separadas por espaço: ").split())

    # Calcula a média ponderada com pesos 2, 3, 4 e 1
    media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

    # Exibe a média com uma casa decimal
    print(f"Média: {media:.1f}")

    # Verifica a situação do aluno com base na média
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        # Caso o aluno esteja em exame
        print("Aluno em exame.")
        nota_exame = float(input("Digite a nota do exame: "))
        print(f"Nota do exame: {nota_exame:.1f}")

        # Recalcula a média final após o exame
        media_final = (media + nota_exame) / 2

        # Verifica se o aluno foi aprovado ou reprovado após o exame
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")

        # Exibe a média final com uma casa decimal
        print(f"Média final: {media_final:.1f}")


# Chamada da função principal
if __name__ == "__main__":
    main()
