print("---Palavra Passe---\n\n")

# User insere os dados
nova_password = input("Crie sua nova password: ")

tentativas = 0
max_tentativas = 5

while tentativas < max_tentativas:
    password = input("Insira a sua password: ")
    if password == nova_password:
        print("Password correta! Acesso concedido.")
        break
    else:
        print("Password errada! Tente novamente.")
        tentativas += 1

if tentativas == max_tentativas:
    print("Conta bloqueada por 24H")
