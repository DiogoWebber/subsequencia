import numpy as np
import matplotlib.pyplot as plt

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = np.zeros((m+1, n+1), dtype=int)

    # Construção da matriz L de maneira bottom-up
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    return L

def plot_lcs_matrix(X, Y, L):
    fig, ax = plt.subplots()
    # Visualização da matriz L com um mapa de cores
    cax = ax.matshow(L, cmap='viridis')
    fig.colorbar(cax)

    # Configuração dos ticks nos eixos x e y
    ax.set_xticks(np.arange(len(Y) + 1))
    ax.set_yticks(np.arange(len(X) + 1))
    ax.set_xticklabels([''] + list(Y))
    ax.set_yticklabels([''] + list(X))

    # Legendas e título
    plt.xlabel('Y')
    plt.ylabel('X')
    plt.title('LCS Matrix')
    plt.show()

X = "AGGTAB"
Y = "GXTXAYB"

# Cálculo da matriz LCS
L = lcs(X, Y)
print(f"O comprimento da subsequência comum mais longa é {L[len(X)][len(Y)]}")

# Visualização da matriz LCS
plot_lcs_matrix(X, Y, L)
