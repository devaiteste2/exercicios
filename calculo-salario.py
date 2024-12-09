def calcula_salario():
    numero_funcionario = int(input("Digite o número do funcionário: "))
    horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
    valor_hora = float(input("Digite o valor da hora trabalhada: "))

    salario = horas_trabalhadas * valor_hora

    print(f"NUMBER = {numero_funcionario}")
    print(f"SALARY = U$ {salario:.2f}")

# Chamada da função (opcional, mas geralmente não necessária)
calcula_salario()
