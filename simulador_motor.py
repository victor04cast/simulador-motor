
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulador de Arranque Lineal de un Motor Eléctrico")

# Parámetros configurables
corriente_inicial = st.number_input("Corriente Inicial (A)", min_value=0.0, value=10.0)
corriente_pico = st.number_input("Corriente Pico (A)", min_value=corriente_inicial, value=50.0)
corriente_trabajo = st.number_input("Corriente de Trabajo (A)", min_value=0.0, value=20.0)
tiempo_total = st.number_input("Tiempo Total de Simulación (s)", min_value=1.0, value=10.0)
rpm_final = st.number_input("RPM Final", min_value=0.0, value=3000.0)

# Simulación de tiempo
tiempo = np.linspace(0, tiempo_total, num=500)

# Simulación de corriente (arranque lineal)
corriente = np.piecewise(
    tiempo,
    [tiempo < tiempo_total / 3, (tiempo >= tiempo_total / 3) & (tiempo < 2 * tiempo_total / 3), tiempo >= 2 * tiempo_total / 3],
    [
        lambda t: corriente_inicial + (corriente_pico - corriente_inicial) * (t / (tiempo_total / 3)),
        lambda t: corriente_pico - (corriente_pico - corriente_trabajo) * ((t - tiempo_total / 3) / (tiempo_total / 3)),
        corriente_trabajo
    ]
)

# Simulación de RPM (lineal)
rpm = rpm_final * (tiempo / tiempo_total)

# Gráfica de corriente vs tiempo
st.subheader("Corriente vs Tiempo")
fig1, ax1 = plt.subplots()
ax1.plot(tiempo, corriente, label="Corriente (A)", color='blue')
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Corriente (A)")
ax1.grid(True)
st.pyplot(fig1)

# Gráfica de RPM vs tiempo
st.subheader("RPM vs Tiempo")
fig2, ax2 = plt.subplots()
ax2.plot(tiempo, rpm, label="RPM", color='green')
ax2.set_xlabel("Tiempo (s)")
ax2.set_ylabel("RPM")
ax2.grid(True)
st.pyplot(fig2)
