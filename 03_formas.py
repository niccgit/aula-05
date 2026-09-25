import math

def circulo ():
    raio = float(input("Digite o valor do Raio do círculo: "))
    area = math.pi * pow(raio, 2)
    print(f"A área do círculo é: {round(area, 2)}")

def triangulo ():
    base = float(input("Digite o valor da Base do triângulo: "))
    altura = float(input("Digite o valor da Altura do triângulo: "))
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def quadrado ():
    lado = float(input("Digite o valor do Lado do quadrado: "))
    area = lado * lado
    print(f"A área do quadrado é: {area}")

def retangulo():
    largura = float(input("Digite o valor da Largura do retângulo: "))
    comprimento = float(input("Digite o valor do Comprimento do retângulo: "))
    area = largura * comprimento
    print(f"A área do retângulo é: {area}")

def paralelogramo():
    base = float(input("Digite o valor da Base do paralelogramo: "))
    altura = float(input("Digite o valor da Altura do paralelogramo: "))
    area = base * altura
    print(f"A área do paralelogramo é: {area}")

def losango():
    maior = float(input("Digite o valor da Maior Diagonal do losango: "))
    menor= float(input("Digite o valor da Menor Diagonal do losango: "))
    area = (maior * menor) / 2
    print(f"A área do losango é: {area}")

def trapezio():
    base_maior = float(input("Digite o valor da Maior Base do trapézio: "))
    base_menor = float(input("Digite o valor da Menor Base do trapézio: "))
    altura = float(input("Digite o valor da Altura do trapézio: "))
    soma = base_maior + base_menor
    area = (soma * altura) / 2
    print(f"A área do trapézio é: {area}")

while True:
   print("Calculador de Área - Formas Geométricas")
   print("1 - Círculo")
   print("2 - Triângulo")
   print("3 - Quadrado")
   print("4 - Retângulo")
   print("5 - Paralelogramo")
   print("6 - Losango")
   print("7 - Trapézio")
   print("0 - Sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      circulo()
   elif opcao == "2":
       triangulo()
   elif opcao == "3":
       quadrado()
   elif opcao == "4":
       retangulo()
   elif opcao == "5":
       paralelogramo()
   elif opcao == "6":
       losango()
   elif opcao == "7":
        trapezio()
   elif opcao == "0":
    print("Saindo do sistema...")
    break
   else:
       print("Opção inválida. Tente novamente!")