'''
v -> velocidade
d -> distância
t -> tempo
'''

print("---Cálculo da velocidade---\n\n")

#User insere os dados
print("Indique o tempo em segundos: ")
t = float(input())

print("Agora à distâcia em metros: ")
d = float(input())

#Cálculo da velocidade
v = d / t

print(f"A sua velocidade é {v} m/s")
