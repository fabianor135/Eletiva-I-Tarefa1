# open("caminho","r")

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

import os
arquivo = open("AULA12/test2.txt", "w")

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# arquivo.write("Python\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")


# arquivo.close()

import os

if os.path.exists("Aula12/test2.txt"):
    os.remove("Aula12/test2.txt")
else :
  print("Arquivo não existe")

os.rmdir("Aula12/nova_pasta")
