import numpy as np
import matplotlib.pyplot as plt

def calcular_RO(total_infectados, total_recuperados, taxa_de_mortalidade, populacao_suscetivel, a, b, tolerancia=1e-6):
    fa = (total_infectados - total_recuperados) / (taxa_de_mortalidade * populacao_suscetivel) - a
    fb = (total_infectados - total_recuperados) / (taxa_de_mortalidade * populacao_suscetivel) - b

    if np.sign(fa) == np.sign(fb):
        print("A função não muda de sinal no intervalo dado.")
        return None

    while np.abs(b - a) > tolerancia:
        c = (a * fb - b * fa) / (fb - fa)
        fc = (total_infectados - total_recuperados) / (taxa_de_mortalidade * populacao_suscetivel) - c

        if np.abs(fc) < tolerancia:
            return c

        if np.sign(fc) == np.sign(fa):
            a = c
            fa = fc
        else:
            b = c
            fb = fc

    return (a + b) / 2

# Parâmetros do modelo
total_infectados = 2882
total_recuperados = 1581
taxa_de_mortalidade = 126 / total_infectados
populacao_suscetivel = 10000
a = 0
b = 10

# Cálculo do RO
RO = calcular_RO(total_infectados, total_recuperados, taxa_de_mortalidade, populacao_suscetivel, a, b)

print("Taxa de Reprodução Básica (RO):", RO)

# Plotagem do gráfico
RO_values = np.linspace(a, b, 100)
y = (total_infectados - total_recuperados) / (taxa_de_mortalidade * populacao_suscetivel) - RO_values

plt.plot(RO_values, y, label='Função')
plt.axhline(y=0, color='r', linestyle='--')
plt.axvline(x=RO, color='g', linestyle='--', label='RO')
plt.xlabel('RO')
plt.ylabel('f(RO)')
plt.title('Gráfico da Função')
plt.legend()
plt.grid(True)
plt.show()