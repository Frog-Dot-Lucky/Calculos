Capital = float(input("Digite o capital inicial: "))
Taxa = float(input("Digite a taxa de juros (em %): ")) / 100

Perda = Capital * Taxa

print(f"perda com a inflação: R${Perda:.2f}")
