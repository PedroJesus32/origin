#f(x) para calcular o peso dum homem
def pM(height):
    pesoM = float(72.7 * height - 58.0)
    print(f"Seu peso ideal é {pesoM} Kg")

#f(x) para calcular o peso duma mulher
def pF(height):
    pesoF = float(62.1 * height - 44.7)
    print(f"Seu peso ideal é {pesoF} Kg")


print("...Peso ideal...\n")

#User insere dados
print("Insira seu gênero (M ou F): ")
genero = input()
height = float(input("Insira sua altura em metros: "))

#Verificar genéro
while(genero != "M" and genero != "F"):
    print("Isso não existe!, coloque" \
    " M ou F: ")
    genero = input()

if(genero == "M"):
    pM(height)
else:
    pF(height)



