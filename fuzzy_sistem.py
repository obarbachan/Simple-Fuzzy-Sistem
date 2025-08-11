import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Definir Universo (faixa de valores)
temperatura = ctrl.Antecedent(np.arange(10, 41, 1), 'temperatura')
velocidade = ctrl.Consequent(np.arange(0, 101, 1), 'velocidade')

# 2. Funções de Pertinência (Triangulares/Trapezoidais)
temperatura['fria'] = fuzz.trimf(temperatura.universe, [10, 10, 25])
temperatura['agradável'] = fuzz.trimf(temperatura.universe, [15, 25, 35])
temperatura['quente'] = fuzz.trimf(temperatura.universe, [25, 40, 40])

velocidade['lenta'] = fuzz.trimf(velocidade.universe, [0, 0, 50])
velocidade['media'] = fuzz.trimf(velocidade.universe, [20, 50, 80])
velocidade['rapida'] = fuzz.trimf(velocidade.universe, [50, 100, 100])

# Visualizar funções
temperatura.view()
velocidade.view()
plt.show()

# 3. Regras Fuzzy
regra1 = ctrl.Rule(temperatura['fria'], velocidade['lenta'])
regra2 = ctrl.Rule(temperatura['agradável'], velocidade['media'])
regra3 = ctrl.Rule(temperatura['quente'], velocidade['rapida'])

# 4. Sistema de Controle
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

# Entrada: Temperatura atual
sistema.input['temperatura'] = 28  # Exemplo

# Executar sistema
sistema.compute()

# Resultado
print(f"Velocidade: {sistema.output['velocidade']:.2f}%")
velocidade.view(sim=sistema)
plt.show()