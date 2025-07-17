print("---Será um ano bissexto?---\n\n")

print("Insira um nº para ver se é" \
"um ano bissexto ou não: ")

ano = int(input())

if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
