# def big_mac():
#     print("sanduiche big mac")


# print("inicio")
# big_mac()
# print("fim")

def fazer_big_mac(nome):
    print(f"sanduiche big mac para {nome}")


# fazer_big_mac("Fabiano")
# fazer_big_mac("Adriana")
# fazer_big_mac("Guilherme")
# fazer_big_mac("Gustavo")


def fazer_batata(tamanho):
    print(f"batata {tamanho}")


def preparar_refrigerante(tipo, tamanho):
    print(f"{tipo} {tamanho}")

# fazer_big_mac("Fabiano")
# fazer_batata("Grande")
# preparar_refrigerante("Coca", "Média")


def fazer_combo_big_mac(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)


# fazer_combo_big_mac("Fabiano", "Grande", "Coca-Cola", "Média")

def soma_num(num1, num2):
    return num1 + num2


# resultado = soma_num(15, 20)
# print(resultado)


def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num


resultado = maior_num([321, 654, -68, 789, 2, 165, -1, -46, 3654, 2, 7])
print(resultado)
