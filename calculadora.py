def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y    

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y        

while True:
    print("selecione o tipo de operação:")
    print("1. Somar")
    print("2. Subtrair")    
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite uma das opções: ")
    if escolha == '1':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", somar(num1, num2))
    elif escolha == '2':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", subtrair(num1, num2))
    elif escolha == '3':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", multiplicar(num1, num2))        
    elif escolha == '4':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("Resultado:", dividir(num1, num2))
    else:
        print("Entrada inválida")

    proximo_calculo = input("Deseja fazer outro cálculo? (digite sim ou não): ")
    if proximo_calculo.lower() != 'sim':
        break
print("Obrigado por usar a calculadora!")
 
