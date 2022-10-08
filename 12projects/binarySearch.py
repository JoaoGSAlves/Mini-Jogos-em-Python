import time
import random

def busca_simples(l,alvo):
    for i in range(len(l)):
        if l[i]== alvo:
            return i

    return -1 

def busca_binaria(l,alvo, low=None,high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1

    midpoint = (low + high) // 2

    if l[midpoint] == alvo:
        return midpoint

    elif alvo < l[midpoint]:
        return busca_binaria(l,alvo,low,midpoint-1)

    else:
        return busca_binaria(l,alvo,midpoint+1,high)



if __name__ == '__main__':
    # l = [1,3,5,10,12,15,18,43,57,79]
    # alvo = 79
    # print(busca_simples(l,alvo))
    # print(busca_binaria(l,alvo))

    tamanho = 10000
    sorted_list = set()
    while len(sorted_list) < tamanho:
        sorted_list.add(random.randint(-3*tamanho,3*tamanho))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for alvo in sorted_list:
        busca_binaria(sorted_list,alvo)
    end = time.time()
    print('Tempo de busca binária : ', (end-start)/tamanho, " segundos")
    
    start = time.time()
    for alvo in sorted_list:
        busca_simples(sorted_list,alvo)
    end = time.time()
    print('Tempo de busca simples : ', (end-start)/tamanho, " segundos")
