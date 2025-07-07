print("---Classificador de notas---\n")

print("Insira a sua nota de 0 à 100: ")
nota = float(input())

while(nota < 0 or nota > 100):
    print("Insira uma nota válida" \
    " de 0 à 100: ")
    nota = float(input()) 

if(nota < 50):
    print(f"Reprovado!->{nota}%")
elif(nota > 50 and nota < 70):
    print(f"Suficiente->{nota}%")
elif(nota > 70 and nota < 90):
    print(f"Bom->{nota}%")
elif(nota > 90 and nota <= 100):
    print(f"Excelente!->{nota}%")

       