produtos = []

def mostrar():
   for x in produtos:
      print(f"Sua lista contém os seguintes itens: {x}")

def cadastro():
    novo_produto = str(input("Digite o nome do produto: "))
    produtos.append(novo_produto)

def excluir():
    deletar = str(input("Digite o nome do item que você deseja excluir: "))
    produtos.remove(deletar)

def modificar():
    modi = int(input("Digite o índice do produto que você deseja alterar: "))
    prod = str(input("Qual produto você deseja adicionar no lugar? "))  
    produtos[modi] = prod     

while True: 
   print("Lista de Compras")
   print("1 - Mostrar a lista")
   print("2 - Cadastrar item na lista")
   print("3 - Excluir item da lista")
   print("4 - Modificar item da lista")
   print("0 - Sair")
   
   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      mostrar()
   elif opcao == "2":
      cadastro()
   elif opcao == "3":
      excluir()
   elif opcao == "4":
      modificar()
   elif opcao == "0":
    print("Saindo do sistema...")
    break
   else:
       print("Opção inválida. Tente novamente!")     