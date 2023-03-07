import numpy as np


def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float - inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """

    n = len(data)
    resultado = 0

    for i in range(n):
        resultado += ((theta_0 + theta_1*data[i][0]) - data[i][1]) ** 2

    resultado = resultado / n

    return resultado


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float - inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    
    n = len(data)
    derParcThe0 = 0
    derParcThe1 = 0
    
    for i in range(n):
        derParcThe0 += ((theta_0 + theta_1*data[i][0]) - data[i][1])
        derParcThe1 += ((theta_0 + theta_1*data[i][0]) - data[i][1]) * data[i][0]

    derParcThe0 = derParcThe0*2 / n
    derParcThe1 = derParcThe1*2 / n 

    theta_0 = theta_0 - alpha*derParcThe0
    theta_1 = theta_1 - alpha*derParcThe1

    return theta_0, theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    
    listaTheta0 = []
    listaTheta1 = []

    for i in range(num_iterations):
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        listaTheta0.append(theta_0)
        listaTheta1.append(theta_1)

        
    return listaTheta0, listaTheta1



quiz_data = np.genfromtxt('alegrete.csv', delimiter=',')

#print(fit(quiz_data, 0, 0, 0.1, 100))