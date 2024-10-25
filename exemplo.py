
import sqlite3

class Ecommerce:
    def __init__(self,db="db.sqlite3"):
        self.conn() = sqlite3.connect
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
                    print("Create")
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
               ttituloProduto,
               preco,
               descricao,
               imgProduto,
               catProduto,
               classProduto,
               exibirNome
               ):
        pass
home = Ecommerce()

# class Carro:
#     def __init__(self,marca,modelo,ano):
#             self.marca = marca
#             self.modelo = modelo
#             self.ano =ano

#     def imprimir(self):
#           return print(f"A marca do carro é {self.marca}, o ano {self.ano} e o modelo é {self.modelo}")

# x = Carro("VW","UP","2016") 
# x.imprimir

# y = Carro("Toyota", "Corola","2022")
# y.imprimir