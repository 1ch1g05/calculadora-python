def somar (a, b)
return a + b
def subtrair (a, b)
return a - b
def multiplicar (a, b)
return a * b
def dividir (a, b)
return a / b
if b == 0:
  return "Error: divisão por zero"
  return a / b
  def calculadora ()
  print("=== Calculadora Avançada ===")
  while true:
    print("\n Escolha uma operação.")
    print("1. somar (+)")
    print("2. subtrair (-)")
    print("3. multiplicar (*)")
    print("4. dividir (/)")
    print("5. sair")
    escolha = input("Digite a opção (1 -5):")
    if escolha == '5':
      print("Opção inválida. Tente novamente.")
      continue
      try:
        num1 = float(input("primeiro número:"))
        num2 = float(input("segundo número:"))
      except value error:
      print("Entrada inválida. Digite números válidos.")
      continue
      if escolha == '1':
      print(f"Resultado: {somar (num1, num2)}")
    elif escolha == '2':
      print(f"Resultado: {subtrair (num1, num2)}")
elif escolha == '3':
print(f"Resultado: {multiplicar (num1, num2)}")
elif escolha == '4':
print(f"Resultado: {dividir (num1, num2)}")
calculadora()
