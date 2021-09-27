idades = [20, 36, 23, 63]
# print('As idades são:', idades)
# print('a quantidade de idades é:', len(idades))
# print('A idade na posição 0 é:', idades[0])
#
# idades.append(15)
# print('Mais a idade 15 na lista', idades)
#
# idades.remove(36)
# print('A idade 36 foi removida da lista', idades)

# idades.clear()
# print('Apaguei todas as idades da lista co o comando clear()', idades)

print(idades)

if 36 in idades:
    idades.remove(36)

print(idades)

if 24 in idades:
    idades.remove(24)

print(idades)


idades.insert(0, 256)
print(idades)

idades.extend([25, 36, 36])

print(idades)

idades_no_ano_que_vem = []
for idade in idades:
    idades_no_ano_que_vem.append(idade+1)
print(idades_no_ano_que_vem)
idades_no_ano_que_vem = [(idade+1) for idade in idades]
print(idades_no_ano_que_vem)

idades_maior_de_21_anos = [(idade) for idade in idades if idade > 21]
print(idades_maior_de_21_anos)
