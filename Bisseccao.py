import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Função que define o modelo SIR
def sir_model(sir, t, beta, gamma):
    S, I, R = sir
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Método de bissecção
def bisect(func, a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Função que define o ponto de equilíbrio
def find_equilibrium(beta, gamma):
    equilibrium_S = gamma / beta
    equilibrium_I = 1 - gamma / beta
    equilibrium_R = 0
    return equilibrium_S, equilibrium_I, equilibrium_R

# Parâmetros do modelo
beta = 0.5
gamma = 0.3

# Encontrando o ponto de equilíbrio
equilibrium = find_equilibrium(beta, gamma)
print("Ponto de equilíbrio: S =", equilibrium[0], "I =", equilibrium[1], "R =", equilibrium[2])

# Gerando gráfico da curva SIR
t = np.linspace(0, 100, 1000)  # Intervalo de tempo
sir_initial = [0.99, 0.01, 0]  # Condições iniciais

# Solução numérica das equações diferenciais
sir_solution = odeint(sir_model, sir_initial, t, args=(beta, gamma))
S = sir_solution[:, 0]
I = sir_solution[:, 1]
R = sir_solution[:, 2]

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Suscetíveis')
plt.plot(t, I, label='Infectados') 
plt.plot(t, R, label='Recuperados')
plt.xlabel('Tempo') 
plt.ylabel('Proporção da População') 
plt.legend()
plt.grid(True)
plt.show()