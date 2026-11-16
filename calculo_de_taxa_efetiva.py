Taxa = float(input("Digite a taxa de juros (em %): ")) / 100
Tempo = float(input("Digite o tempo (em meses): "))

Taxa_Efetiva = ((1 + Taxa) ** Tempo - 1) * 100

print(f"Taxa efetiva total: {Taxa_Efetiva:.2f}%")
