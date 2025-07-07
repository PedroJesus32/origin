print("Quêm é o mais velho\n\n")

print("Insira seu nome: ")
nome_1 = str(input())
print("Sua idade: ")
idade_1 = int(input())

print("Agora a outra pessoa\n"
      "Seu nome: ")
nome_2 = str(input())
print("Sua idade: ")
idade_2 = int(input())

if(idade_1 > idade_2):
    print(f"{nome_1} é mais velho "
          f"do que {nome_2}.")
elif(idade_1 < idade_2):
        print(f"{nome_2} é mais velho "
          f"do que {nome_1}.")
else:
        print("Ambas têm a mesma idade.")
