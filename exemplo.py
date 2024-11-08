import sqlite3
import pandas as pd

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
                    self.read()
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
            VALUES(?,?,?,?,?,?,?)''',#Onde é Inserido as informações de produto
            (tituloProduto,
            preco,
            descricao,
            imgProduto,
            catProduto,
            classProduto,
            exibirNome))
        self.conn.commit()
        print("Produto cadastrado com sucesso!!")

    def menu_create(self): #metodo que vai ser olhado por todo objeto
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
        titulo = input("TItulo: ")
        preco = float(input("Preço: "))
        descricao = input("Descrição: ")
        imagemProduto = input("Imagem: ")
        catProduto = input("Categoria: ")
        classProduto = input("Classificação: ")
        exibirNome = input("Exibir( True, False): ")
        self.create(titulo, preco, descricao, imagemProduto, catProduto, classProduto, exibirNome)

    def read(self):
        print("\n"
              "[1] - Lista todos os produtos\n"
              "[2]- Listar por ID's"

              )
        op = int(input("Escolha a opção:"))
        match op:
            case 1:
                df = pd.read_sql_query("SELECT * FROM api_produto", self.conn)
                return print(df)
                
            case 2:
                valor = int(input("ID:"))
                query = f"SELECT * FROM  api_produto WERE id = {valor}"
                df = pd.read_sql_query(query, self.conn)
                return print(query)
            case _:
                print("Escolha a opção válida")

home = Ecommerce()