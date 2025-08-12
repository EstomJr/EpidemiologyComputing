import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Função que define as equações diferenciais do modelo SEIR
# y: vetor com os valores de S, E, I, R
# t: tempo
# N: população total
# beta: taxa de transmissão
# sigma: taxa de progressão (Exposto -> Infectado)
# gamma: taxa de recuperação
def seir_model(y, t, N, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# ---- 1. Definição dos Parâmetros e Condições Iniciais ----

# População total
N = 1000000

# Parâmetros epidemiológicos da COVID-19
R0_val = 3.0                 # Número básico de reprodução
periodo_incubacao = 5.0      # Período de incubação (latência) em dias
periodo_infeccioso = 7.0     # Duração da infecção em dias

# Cálculo das taxas do modelo
sigma = 1.0 / periodo_incubacao   # Taxa de progressão E -> I (1/dias)
gamma = 1.0 / periodo_infeccioso  # Taxa de recuperação I -> R (1/dias)
beta = R0_val * gamma             # Taxa de transmissão (R0 = beta / gamma)

# Condições iniciais
E0 = 1  # Inicia com 1 indivíduo exposto (no período de latência)
I0 = 0  # Nenhum indivíduo infeccioso no instante zero
R0 = 0  # Nenhum indivíduo recuperado no instante zero
S0 = N - E0 - I0 - R0 # Número inicial de suscetíveis

# Vetor de condições iniciais para o solver
y0 = S0, E0, I0, R0

# Grid de tempo (em dias) para a simulação
dias = 150
t = np.linspace(0, dias, dias)

# ---- 2. Solução do Sistema de Equações Diferenciais ----

# Integração do modelo SEIR ao longo do tempo
solution = odeint(seir_model, y0, t, args=(N, beta, sigma, gamma))
S, E, I, R = solution.T # Separa as soluções para cada compartimento

# ---- 3. Visualização dos Resultados ----

# Criação do gráfico
plt.figure(figsize=(12, 8))
plt.plot(t, S, 'b', label='Suscetíveis (S)')
plt.plot(t, E, color='orange', linestyle='--', label='Expostos (E)')
plt.plot(t, I, 'r', label='Infectados (I)')
plt.plot(t, R, 'g', label='Recuperados (R)')

# Configurações do gráfico
plt.title('Implementação do Modelo SEIR para Surto de COVID-19')
plt.xlabel('Tempo (dias)')
plt.ylabel('Número de Indivíduos')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Imprime os valores dos parâmetros para referência
print(f"Parâmetros da Simulação:")
print(f"População Total (N): {N}")
print(f"Número Básico de Reprodução (R0): {R0_val}")
print(f"Taxa de Transmissão (beta): {beta:.4f}")
print(f"Taxa de Progressão (sigma): {sigma:.4f} (Período de Incubação: {periodo_incubacao} dias)")
print(f"Taxa de Recuperação (gamma): {gamma:.4f} (Período Infeccioso: {periodo_infeccioso} dias)")
