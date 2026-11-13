Capital = float(input("Digite o capital inicial: "))
Taxa = float(input("Digite a taxa de juros (em %)")) / 100
Tempo = float(input("Digite o tempo (em meses): "))

Juros = Capital * Taxa * Tempo

Montante = Capital + Juros

print(f"juros ganhos: R${Juros:.2f}")
print(f"montante total: R${Montante:.2f}")
