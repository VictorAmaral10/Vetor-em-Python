n = int(input("Quantos números você vai digitar? "))

vet:[float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um número: "))

print()
print("NUMEROS DIGITADOS:")

for i in range(0, n):
    print("{:.1f}".format(vet[i]))