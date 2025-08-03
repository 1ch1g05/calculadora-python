#Calculadora Simples - Versão Básica
print("=== Calculadora ===")
print("Operações disponíveis: +, -, *, /")
#Entrada de dados
num1 = float(input("Digite o peimeiro número:"))
operacao = input("Digite a operações(+, -, *, /):")
num2 = float(input("Digite o segundo número:"))
#Cálculo com base na operação
if operacao == '+':
    resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
            elif operacao == '/':
                if num2 != 0
                resultado = num1 / num2
                else:
                    print("Erro: Divisão por zero não é permitida.")
                    resultado = None
                    else: 
                        print("Operação inválida!")
                        resultado = None
                        
  #Exibir resultado válido
  if resultado is not None:
                print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
