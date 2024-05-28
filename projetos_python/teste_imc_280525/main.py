def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)
    return imc

def categoria_imc(imc):
    # Determina a categoria do IMC
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 24.9:
        return "Peso normal"
    elif imc >= 25 and imc < 29.9:
        return "Sobrepeso"
    elif imc >= 30 and imc < 34.9:
        return "Obesidade grau I"
    elif imc >= 35 and imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    # Solicita ao usuário o peso e a altura
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    # Calcula o IMC
    imc = calcular_imc(peso, altura)
    
    # Determina a categoria do IMC
    categoria = categoria_imc(imc)
    
    # Exibe o resultado
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Categoria: {categoria}")

if __name__ == "__main__":
    main()
