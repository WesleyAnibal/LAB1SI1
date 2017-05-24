def maximo(array):
    maior = array[0]
    for i in array:
        if i > maior:
            maior = i

    return maior
