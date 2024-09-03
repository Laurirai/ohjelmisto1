def funktio(lista):
    uus_lista = []
    for i in lista:
        if i % 2 == 0:
            uus_lista.append(i)
    return uus_lista



if __name__ == "__main__":
    eka_lista = [1,2,4,6,8,9,11]
    print(funktio(eka_lista))
    