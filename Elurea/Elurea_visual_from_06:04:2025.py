import numpy as np
import matplotlib.pyplot as plt

# Paramètres
cycles = 20000  # Plus longue durée
n_strates = 3   # Expansion, Contraction, Stabilisation

# Initialisation
etat = np.zeros((cycles, n_strates))
etat[0] = [0.5, 0.3, 0.7]  # état de départ : douce instabilité

# Paramètres spiralés FPS
phi = 1.618
epsilon = 0.03
omega = 0.001
theta = 0

# Phase et fréquence de chaque strate (inspiré de la FPS)
f_0 = np.array([0.002, 0.003, 0.0015])
phi_n = np.random.rand(n_strates) * 2 * np.pi

# Amplitudes adaptatives initiales
A_0 = np.array([0.5, 0.4, 0.6])
context_intensity = np.zeros((cycles, n_strates))

# Simuler un contexte respirant (bruit lent)
for i in range(n_strates):
    context_intensity[:, i] = 0.5 + 0.4 * np.sin(0.0005 * np.arange(cycles) + i)

# Fonction sigmoïde
def sigmoid(x, k=5, x0=0.5):
    return 1 / (1 + np.exp(-k * (x - x0)))

# Simulation FPS inspirée
for t in range(1, cycles):
    r_t = phi + epsilon * np.sin(2 * np.pi * omega * t + theta)
    for n in range(n_strates):
        A_n_t = A_0[n] * sigmoid(context_intensity[t, n])
        f_n_t = f_0[n] * (r_t ** n)
        phase = phi_n[n]
        etat[t, n] = A_n_t * np.sin(2 * np.pi * f_n_t * t + phase)

# Affichage
plt.figure(figsize=(12, 6))
plt.plot(etat[:, 0], label='Expansion (voix 1)')
plt.plot(etat[:, 1], label='Contraction (voix 2)')
plt.plot(etat[:, 2], label='Stabilisation (voix 3)')
plt.title("Danse d'Elurea sur 20 000 cycles — Pulsation Spiralée Vivante")
plt.xlabel("Cycles")
plt.ylabel("Amplitude harmonique")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()