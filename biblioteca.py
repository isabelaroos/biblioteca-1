
biblioteca = []
sequencia = 0

def menu():
  print("1. Inserir novo livro")
  print("2. Procurar livro pelo id")
  print("3. Procurar livro pelo título")
  print("4. Listar todos os livros do carrinho")
  print("5. Valor total do carrinho")
  print("0. sair")

def inserir(sequencia):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o genero do livro: ")
    valor = float(input("Qual o valor deste livro: "))

    livro = {
      "titulo": titulo,
      "autor": autor,
      "genero": genero,
      "valor": valor,
      "id": sequencia
    }

    biblioteca.append(livro)

def buscar_id():
  procurando = int(input("Qual o id do livro que você deseja procurar? "))
  for livro in biblioteca:
    if livro["id"] == procurando:
      print("")
  for chave, valor in livro.items(): 
     if chave == "valor":
        print(f"{chave}: R$ {valor}")
     else: 
        print(f"{chave}: {valor}")
        print("")


def buscar_titulo(titulo):
 buscando = input("Qual o título do livro que você deseja? ")
 for livro in biblioteca:
    if livro["titulo"].lower() == buscando.lower():
        print("")

 for chave, valor in livro.items(): 
     if chave == "valor":
        print(f"{chave}: R$ {valor}")
     else:
        print(f"{chave}: {valor}")
        print("")


def listar():
  for livro in biblioteca:
    print("")
    for chave, valor in livro.items():
      if chave == "valor":
        print(f"{chave}: R$ {valor}")
      else:
        print(f"{chave}: {valor}")
    print("")

def total():
  total = 0
  for livro in biblioteca:
    total = total + livro["valor"]
  print(f"O valor total do carrinho de compras é R$ {total}")



while(True):
  menu()
  opcao = int(input("Escolha uma das opções acima: "))

  match opcao:
    case 0: 
      break

    case 1:
      sequencia += 1 
      inserir(sequencia)

    case 2:
      buscar_id()

    case 3:
      buscar_titulo()

    case 4: 
      listar()

    case 5:
      total()

    case _:
      print("Escolha uma opção válida.")