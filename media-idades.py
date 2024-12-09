def calcular_media_idades():
    soma_idades = 0
    quantidade = 0

    while True:
        try:
           
            idade = int(input("Digite uma idade (ou um valor negativo para encerrar): "))
            
            
            if idade < 0:
                break
            
            
            soma_idades += idade
            quantidade += 1
        
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")
    
    
    if quantidade > 0:
        media = soma_idades / quantidade
        return round(media, 2)
    else:
        return "Nenhuma idade válida foi inserida."

def main():
    try:
        
        media_idades = calcular_media_idades()
        
        
        print(f"A média das idades é: {media_idades}")
    
    except Exception as e:
        print(f"Erro: {e}")


    main()

