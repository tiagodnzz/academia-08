nome = input("Digite seu nome: ").lower()
idade = int(input("Digite sua idade:"))

if (nome == "dougras" and idade == 22) or nome == "douglas":
    print("Eu sou o Dougras")
elif nome == "tiago" and idade == 18:
    print("Salve Tiago mlk lindo")
else:
    print("Voce não é o Dougras")

numero = 0
while numero < 5:
    print(numero)
    numero = numero +1

lista = ["cubo magico","pagode japones", "skate", "manga com leite"]
for item in lista:
    print(item)

for i in range(len(lista)):
    print(lista[i])