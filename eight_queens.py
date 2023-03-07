from random import *
import matplotlib.pyplot as plt


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    #raise NotImplementedError  # substituir pelo seu codigo

    tam = len(individual)
    conflitos = 0

    for i in range(tam):
        diag = 1
        for j in range(i+1, tam):
            if individual[i] == individual[j]:
                conflitos += 1
            elif individual[j] == individual[i] + diag:
                conflitos += 1
            elif individual[j] == individual[i] - diag:
                conflitos += 1
            diag += 1
    
    return conflitos


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """

    melhor = participants[0]
    
    for i in range(1, len(participants)):
        if evaluate(participants[i]) < evaluate(melhor):
            melhor = participants[i]

    return melhor


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    aux = parent1[0:index]
    aux2 = parent2[index: len(parent2)]
    aux.extend(aux2)

    aux3 = parent2[0:index]
    aux4 = parent1[index: len(parent1)]
    aux3.extend(aux4)

    return [aux, aux3]



def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random() < m:
        posAleatoria = randint(0, 7)
        numAleatorio  = randint(1, 8)
        individual[posAleatoria] = numAleatorio

    return individual


def aleatorios(n):
    populacao = []

    for i in range(n):
        aux = 8 * [0]
        for j in range(8):
            aux[j] = randint(1, 8)
        populacao.append(aux)

    return populacao


def valores_grafico(P):

    conflitos = []
    media = 0
    tamanho = len(P)

    for i in range(1, tamanho):
        conflito = evaluate(P[i])
        conflitos.append(conflito)
        media += conflito

    media = media / tamanho
    melhor = min(conflitos)
    pior = max(conflitos)
    
    return [melhor, pior, media]




def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo

    :return:list - melhor individuo encontrado
    """
    melhor=[]
    pior=[]
    media=[]
    
    P = aleatorios(n)


    for i in range(g):
        Px = []
        Px.append(tournament(P))
        while len(Px) < n:
            P1 = tournament(P)
            P2 = tournament(P)
            O1, O2 = crossover(P1, P2, 3)
            O1 = mutate(O1, m)
            O2 = mutate(O2, m)
            Px.append(O1)
            Px.append(O2)

        P = Px
        
        aux1, aux2, aux3 = valores_grafico(P)
        melhor.append(aux1)
        pior.append(aux2)
        media.append(aux3)

    fig, ax = plt.subplots()

    ax.set_xlabel("Generations")
    ax.set_ylabel("Fitness Score")
    ax.plot(melhor, label="Min Fitness")
    ax.plot(pior, label="Max Fitness")
    ax.plot(media, label="Average Fitness")
    ax.set_ylim(0, 20)
    ax.legend()
    ax.grid()
    plt.show()


    return tournament(P)



run_ga(35, 32, 17, 0.81, 1)