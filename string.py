#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
def verificar_letra_a(string):
    string_lower = string.lower()
    count = string_lower.count('a')
    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Digite uma string: ")

verificar_letra_a(texto)
