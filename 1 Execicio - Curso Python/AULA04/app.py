minha_string = " qualquer texto "

print(minha_string.upper())  # Deixa todas letras maisucula
print(minha_string.lower())  # Deixa todas letras minuscula
print(minha_string.capitalize())  # Deixa a primeira letra minuscula
print(minha_string.islower())  # Booleano Verefica se a letra esta em minuscula
print(minha_string.strip())  # Remove espaço do texto
print(minha_string.replace("qualquer", "Meu"))  # Substitui texto
print(minha_string.replace("u", "U"))
print(minha_string.replace("u", "U", 1))
print(minha_string[1])
print(minha_string[2:3])
print(minha_string.index("u"))

x = "texto" in minha_string
print(x)

minha_string = """ linha 1,\"linha 2\",linha 3."""

print(minha_string)
