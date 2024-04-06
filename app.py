pip install skfuzzy

import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

finance = st.number_input("경제적 피해", min_value=0, max_value=100, step=5)
emotion = st.number_input("정서적 피해", min_value=0, max_value=100, step=5)

finance_weight = ctrl.Antecedent(np.arange(0, 101, 1), 'finance weight')
emotion_weight = ctrl.Antecedent(np.arange(0, 101, 1), 'emotion weight')

finance_low = st.number_input("작은 경제적 피해", min_value=0, max_value=100, step=5)
finance_medium = st.number_input("중간 경제적 피해", min_value=0, max_value=100, step=5)
finance_high = st.number_input("큰 경제적 피해", min_value=0, max_value=100, step=5)

finance_weight['low'] = fuzz.trimf(finance_weight.universe, [0, finance_low, finance_medium])
finance_weight['medium'] = fuzz.trimf(finance_weight.universe, [0, finance_medium, finance_high])
finance_weight['high'] = fuzz.trimf(finance_weight.universe, [finance_medium, finance_high, 100])

emotion_low = st.number_input("작은 정서적 피해", min_value=0, max_value=100, step=5)
emotion_medium = st.number_input("중간 정서적 피해", min_value=0, max_value=100, step=5)
emotion_high = st.number_input("큰 정서적 피해", min_value=0, max_value=100, step=5)

emotion_weight['low'] = fuzz.trimf(emotion_weight.universe, [0, emotion_low, emotion_medium])
emotion_weight['medium'] = fuzz.trimf(emotion_weight.universe, [0, emotion_medium, emotion_high])
emotion_weight['high'] = fuzz.trimf(emotion_weight.universe, [emotion_medium, emotion_high, 100])

punishment = ctrl.Consequent(np.arange(0, 101, 1), 'punishment')

punishment_low = st.number_input("작은 처벌", min_value=0, max_value=100, step=5)
punishment_medium = st.number_input("중간 처벌", min_value=0, max_value=100, step=5)
punishment_high = st.number_input("큰 처벌", min_value=0, max_value=100, step=5)

punishment['low'] = fuzz.trimf(punishment.universe, [0, 0, 50])
punishment['medium'] = fuzz.trimf(punishment.universe, [0, 50, 100])
punishment['high'] = fuzz.trimf(punishment.universe, [50, 100, 100])

rule1 = ctrl.Rule(finance_weight['low'] & emotion_weight['low'], punishment['low'])
rule2 = ctrl.Rule(finance_weight['low'] & emotion_weight['medium'], punishment['low'])
rule3 = ctrl.Rule(finance_weight['low'] & emotion_weight['high'], punishment['medium'])
rule4 = ctrl.Rule(finance_weight['medium'] & emotion_weight['low'], punishment['low'])
rule5 = ctrl.Rule(finance_weight['medium'] & emotion_weight['medium'], punishment['high'])
rule6 = ctrl.Rule(finance_weight['medium'] & emotion_weight['high'], punishment['high'])
rule7 = ctrl.Rule(finance_weight['high'] & emotion_weight['low'], punishment['medium'])
rule8 = ctrl.Rule(finance_weight['high'] & emotion_weight['medium'], punishment['high'])
rule9 = ctrl.Rule(finance_weight['high'] & emotion_weight['high'], punishment['high'])


control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
simulation = ctrl.ControlSystemSimulation(control_system)

simulation.input['finance weight'] = finance
simulation.input['emotion weight'] = emotion

simulation.compute()

punishment_value = simulation.output['punishment']  
st.header(punishment_value)


# Matplotlib 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(finance_weight.universe, fuzz.trimf(finance_weight.universe, [0, finance_low, finance_medium]), 'b', linewidth=1.5, label='Finance Low')
plt.plot(finance_weight.universe, fuzz.trimf(finance_weight.universe, [0, finance_medium, finance_high]), 'g', linewidth=1.5, label='Finance Medium')
plt.plot(finance_weight.universe, fuzz.trimf(finance_weight.universe, [finance_medium, finance_high, 100]), 'r', linewidth=1.5, label='Finance High')
plt.plot(emotion_weight.universe, fuzz.trimf(emotion_weight.universe, [0, emotion_low, emotion_medium]), 'c--', linewidth=1.5, label='Emotion Low')
plt.plot(emotion_weight.universe, fuzz.trimf(emotion_weight.universe, [0, emotion_medium, emotion_high]), 'm--', linewidth=1.5, label='Emotion Medium')
plt.plot(emotion_weight.universe, fuzz.trimf(emotion_weight.universe, [emotion_medium, emotion_high, 100]), 'y--', linewidth=1.5, label='Emotion High')
# plt.plot(punishment.universe, fuzz.trimf(punishment.universe, [0, 0, 50]), 'b--', linewidth=1.5, label='Punishment Low')
# plt.plot(punishment.universe, fuzz.trimf(punishment.universe, [0, 50, 100]), 'g--', linewidth=1.5, label='Punishment Medium')
# plt.plot(punishment.universe, fuzz.trimf(punishment.universe, [50, 100, 100]), 'r--', linewidth=1.5, label='Punishment High')
plt.legend()

# 그래프를 Streamlit 애플리케이션에 표시
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)


code = '''
import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

finance = st.number_input("경제적 피해", min_value=0, max_value=100, step=5)
emotion = st.number_input("정서적 피해", min_value=0, max_value=100, step=5)

finance_weight = ctrl.Antecedent(np.arange(0, 101, 1), 'finance weight')
emotion_weight = ctrl.Antecedent(np.arange(0, 101, 1), 'emotion weight')

finance_low = st.number_input("작은 경제적 피해", min_value=0, max_value=100, step=5)
finance_medium = st.number_input("중간 경제적 피해", min_value=0, max_value=100, step=5)
finance_high = st.number_input("큰 경제적 피해", min_value=0, max_value=100, step=5)

finance_weight['low'] = fuzz.trimf(finance_weight.universe, [0, finance_low, finance_medium])
finance_weight['medium'] = fuzz.trimf(finance_weight.universe, [0, finance_medium, finance_high])
finance_weight['high'] = fuzz.trimf(finance_weight.universe, [finance_medium, finance_high, 100])

emotion_low = st.number_input("작은 정서적 피해", min_value=0, max_value=100, step=5)
emotion_medium = st.number_input("중간 정서적 피해", min_value=0, max_value=100, step=5)
emotion_high = st.number_input("큰 정서적 피해", min_value=0, max_value=100, step=5)

emotion_weight['low'] = fuzz.trimf(emotion_weight.universe, [0, emotion_low, emotion_medium])
emotion_weight['medium'] = fuzz.trimf(emotion_weight.universe, [0, emotion_medium, emotion_high])
emotion_weight['high'] = fuzz.trimf(emotion_weight.universe, [emotion_medium, emotion_high, 100])

punishment = ctrl.Consequent(np.arange(0, 101, 1), 'punishment')

punishment_low = st.number_input("작은 처벌", min_value=0, max_value=100, step=5)
punishment_medium = st.number_input("중간 처벌", min_value=0, max_value=100, step=5)
punishment_high = st.number_input("큰 처벌", min_value=0, max_value=100, step=5)

punishment['low'] = fuzz.trimf(punishment.universe, [0, 0, 50])
punishment['medium'] = fuzz.trimf(punishment.universe, [0, 50, 100])
punishment['high'] = fuzz.trimf(punishment.universe, [50, 100, 100])

rule1 = ctrl.Rule(finance_weight['low'] & emotion_weight['low'], punishment['low'])
rule2 = ctrl.Rule(finance_weight['low'] & emotion_weight['medium'], punishment['low'])
rule3 = ctrl.Rule(finance_weight['low'] & emotion_weight['high'], punishment['medium'])
rule4 = ctrl.Rule(finance_weight['medium'] & emotion_weight['low'], punishment['low'])
rule5 = ctrl.Rule(finance_weight['medium'] & emotion_weight['medium'], punishment['high'])
rule6 = ctrl.Rule(finance_weight['medium'] & emotion_weight['high'], punishment['high'])
rule7 = ctrl.Rule(finance_weight['high'] & emotion_weight['low'], punishment['medium'])
rule8 = ctrl.Rule(finance_weight['high'] & emotion_weight['medium'], punishment['high'])
rule9 = ctrl.Rule(finance_weight['high'] & emotion_weight['high'], punishment['high'])


control_system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
simulation = ctrl.ControlSystemSimulation(control_system)

simulation.input['finance weight'] = finance
simulation.input['emotion weight'] = emotion

simulation.compute()

punishment_value = simulation.output['punishment']  
st.header(punishment_value)


# Matplotlib 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(finance_weight.universe, fuzz.trimf(finance_weight.universe, [0, finance_low, finance_medium]), 'b', linewidth=1.5, label='Finance Low')
plt.plot(finance_weight.universe, fuzz.trimf(finance_weight.universe, [0, finance_medium, finance_high]), 'g', linewidth=1.5, label='Finance Medium')
plt.plot(finance_weight.universe, fuzz.trimf(finance_weight.universe, [finance_medium, finance_high, 100]), 'r', linewidth=1.5, label='Finance High')
plt.plot(emotion_weight.universe, fuzz.trimf(emotion_weight.universe, [0, emotion_low, emotion_medium]), 'c--', linewidth=1.5, label='Emotion Low')
plt.plot(emotion_weight.universe, fuzz.trimf(emotion_weight.universe, [0, emotion_medium, emotion_high]), 'm--', linewidth=1.5, label='Emotion Medium')
plt.plot(emotion_weight.universe, fuzz.trimf(emotion_weight.universe, [emotion_medium, emotion_high, 100]), 'y--', linewidth=1.5, label='Emotion High')
# plt.plot(punishment.universe, fuzz.trimf(punishment.universe, [0, 0, 50]), 'b--', linewidth=1.5, label='Punishment Low')
# plt.plot(punishment.universe, fuzz.trimf(punishment.universe, [0, 50, 100]), 'g--', linewidth=1.5, label='Punishment Medium')
# plt.plot(punishment.universe, fuzz.trimf(punishment.universe, [50, 100, 100]), 'r--', linewidth=1.5, label='Punishment High')
plt.legend()

# 그래프를 Streamlit 애플리케이션에 표시
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
'''
st.code(code, language='Python')
