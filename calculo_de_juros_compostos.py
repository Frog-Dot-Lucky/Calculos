capital = float(input("Digite o capital inicial: "))
taxa = float(input("Digite a taxa de juros (em %): ")) / 100
meses = float(input("Digite o tempo (em meses): "))

Montante = capital * (1+taxa) ** meses

juros = Montante - capital

print(f"montante final: R${Montante:.2f}")
print(f"juros ganhos: R${juros:.2f}")
