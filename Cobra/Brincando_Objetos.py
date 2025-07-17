class Turmas:
    def __init__(self):
        self.nomes = []
        self.medias = []
        self.turma = []  # Ex:8ºC
        self.n_notas = int(0)
        self.n_alunos = int(0)


turmax = Turmas()  # Instância da classe Turmas

print("---Avaliador de Notas 2000---\n")

turmax.n_alunos = int(input("Insira o nº de alunos: "))
while turmax.n_alunos < 0:
    turmax.n_alunos = int(input("Insira um nº de alunos " "maior que 0!!!: "))

turmax.n_notas = int(input("Insira a quantidade de notas: "))
while turmax.n_notas < 0:
    turmax.n_alunos = int(input("Insira um nº de notas " "maior que 0!!!: "))

# f(x) para inserir os alunos e as turmas de cada um
for i in range(turmax.n_alunos):
    nome = input(f"Insira o nome do {i + 1}º aluno: ")
    turmax.nomes.append(nome)
    id_turma = input("Insira a sua turma: ")
    turmax.turma.append(id_turma)
    print("\n")

# Iserção das notas e cálculo da média
for i in range(turmax.n_alunos):
    cont = int(1)
    soma_notas = int(0)
    for j in range(turmax.n_notas):
        while cont <= turmax.n_notas:
            nota = int(input(f"Insira à {cont}º nota do {turmax.nomes[i]}: "))
            soma_notas += nota
            cont += 1
    print("\n")
    media = soma_notas / turmax.n_notas
    turmax.medias.append(media)

print("\n")  # Para ficar mais legível

# f(x) para mostrar os resultados
for i in range(turmax.n_alunos):
    print(
        f"{i + 1}º Aluno\n Nome: {turmax.nomes[i]} \n Média: {turmax.medias[i]:.2f}\n"
    )

# f(x) para ver se passou ou não
for i in range(turmax.n_alunos):
    if turmax.medias[i] < 9.5:
        print(f"Alun@ {turmax.nomes[i]} chumbou com {turmax.medias[i]:.2f}")

    elif turmax.medias[i] >= 9.5:
        print(f"Alun@ {turmax.nomes[i]} passou com {turmax.medias[i]:.2f}")
