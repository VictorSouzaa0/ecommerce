import sqlite3

class Ecommerce:
    def __init__(self,db="db.sqlite3"):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
        while True:
            print("\n"
              "[1]- Create\n"
              "[2]- Read\n"
              "[3]- Update\n"
              "[4]- Delete\n"
              "[5]- Exit\n\n"
              )
            op = input("Escolha uma opção: ")

            match op:
                case "1":
                    self.menu_create()
                case "2":
                    print("Read")
                case "3":
                    print("Update")
                case "4":
                    print("Delete")
                case "5":
                    break
                case _:
                    print("Escolha uma opção correta")
    def create(self,
               tituloProduto,
               preco,
               descricao,
               imgProduto,
               catProduto,
               classProduto,
               exibirNome
               ):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO api_produto(
            tituloProduto,
            preco,
            descricao,
            imgProduto,
            catProduto,
            classProduto,
            exibirNome)
            VALUES(?,?,?,?,?,?,?)''',
            (tituloProduto,
            preco,
            descricao,
            imgProduto,
            catProduto,
            classProduto,
            exibirNome))
        self.conn.commit()
        print("Produto cadastrado com sucesso!!")

    def menu_create(self):
        print(
        '\n'
        '[1] - Título \n'
        '[2] - Preço\n'
        '[3] - Descrição\n'
        '[4] - Imagem\n'
        '[5] - Categoria\n'
        '[6] - Classificação\n'
        '[7] - Exibir\n'
    )
        titulo = input("TItulo")
        preco = float(input("Preço: "))
        descricao = input("Descrição: ")
        imagemProduto = input("Imagem: ")
        catProduto = input("Categoria: ")
        classProduto = input("Classificação: ")
        exibirNome = input("Exibir( True, False): ")
        self.create(titulo, preco, descricao, imagemProduto, catProduto, classProduto, exibirNome)

home = Ecommerce()