class Pessoas():
    olhos = 2
    nariz = 1
    orelhas = 2


    def __init__(self, nome, sexo, idade, altura):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.altura = altura

    # def comer(self):
    #     print("Comi")
    # def fazer_som(self):
    #     print("Som")

# mamifero.comer()
pessoas = Pessoa("Amélia","Feminino", 24, 1.60)

pessoa2 = Pessoa("Tiago","Masculino", 18, 1.75)

print(pessoa.nome, pessoa.idade)

print(pessoa2.nome, pessoa.idade)