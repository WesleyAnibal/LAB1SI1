def maximo(array):
    maior = array[0]
    for i in array:
        if i > maior:
            maior = i

    return maior

def minimo(array):
    menor = array[0]
    for i in array:
        if i < menor:
            menor = i

    return menor

