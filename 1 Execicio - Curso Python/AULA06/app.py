familia = ["Fabiano", "Adriana", "Vera", "Miguel"]
#              0          1         2        3
#              -4        -3        -2       -1

# print(familia[1])
# print(familia[-3])
# print(familia[2:])
# print(familia[3:])
# print(familia[-3])

# print(familia)
# familia[2] = "Vera Lucia"
# familia[3] = "Miguel Olivares"
# print(familia)

# familia.extend(["Regina", "Maria Eugenia"])
# print(familia)

# familia.append("Hadesh")
# familia.insert(2, "Hadesh")
# familia.remove("Hadesh") remove o item nomeado da lista
# familia.pop()  # .pop remove o ultimo item da lista


# familia.clear() limpa lista

# print(familia)

# print(familia.index("Adriana"))
# print(familia.count("Vera"))

# idade_familia = [43, 53, 17, 61, 59, 55, 65]
# print(idade_familia)
# idade_familia.sort()
# familia.sort()
# familia.sort()
# familia.reverse()
# print(familia)

familia2 = familia.copy()
print(familia2)
familia.remove("Fabiano")
print(familia)
print(familia2)

coordenadas = (-49, -33)
print(coordenadas.count(-49))
