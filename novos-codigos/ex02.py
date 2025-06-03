
# Código para calcular o IMC (Índice de Massa Corporal)

# Variáveis para peso (kg) e altura (m)
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
