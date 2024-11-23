import streamlit as st
import joblib

# Cargar el modelo entrenado
modelo_entrenado = joblib.load('modelo_entrenado.joblib')

# Título de la aplicación
st.title("Aplicación para predicción del índice de masa corporal (IMC)")

# Crear las opciones para las entradas del usuario

# Edad (valor numérico)
edad = st.slider("Selecciona tu edad:", min_value=1, max_value=100, value=25)

# Nivel de glucosa promedio
glucosa = st.slider("Selecciona tu nivel de glucosa:", min_value=1, max_value=300, value=25)

# Hipertensión (0 = No, 1 = Sí)
hipertension = st.selectbox("Pon 0 si no tienes hipertensión o 1 si tienes", ["0", "1"])

# Cardiopatía (0 = No, 1 = Sí)
cardiopatia = st.selectbox("Selecciona 1 si padeces alguna cardiopatía o 0 si no", ["0", "1"])

# ACV
acv = st.selectbox("Selecciona 1 si sufriste un ACV o 0 si no", ["0", "1"])

# Hábito de fumar
opciones_fumar = ["Never smoked", "Smokes", "No smokes", "Formerly smoked"]
humo = st.selectbox("Selecciona el hábito de consumo de tabaco que posees", opciones_fumar)

# Convertir las entradas a valores numéricos

# Convertir hipertensión y cardiopatía a 0 o 1
hipertension_valor = int(hipertension)
cardiopatia_valor = int(cardiopatia)
acv_valor = int(acv)

# Convertir hábito de fumar en valores numéricos (todas las variables)
if humo == "Never smoked":
    never_smoked = 1
    no_smokes = 0
    formerly_smoked = 0
    smokes = 0
elif humo == "No smokes":
    never_smoked = 0
    no_smokes = 1
    formerly_smoked = 0
    smokes = 0
elif humo == "Formerly smoked":
    never_smoked = 0
    no_smokes = 0
    formerly_smoked = 1
    smokes = 0
else:  # "Smokes"
    never_smoked = 0
    no_smokes = 0
    formerly_smoked = 0
    smokes = 1

# Asegurarse de que las entradas sean números
caracteristicas = [
    float(edad),  # Convertir edad a flotante
    float(glucosa),
    int(hipertension_valor),  # Hipertensión como entero
    int(cardiopatia_valor),  # Cardiopatía como entero
    int(formerly_smoked),  # Fumar anteriormente como entero
    int(never_smoked),  # Nunca fumado como entero
    int(no_smokes),  # No fuma como entero
    int(smokes), # Fuma como entero
    int(acv_valor)
]

# Mostrar el resultado de la predicción (en este caso IMC)
prediccion_imc = modelo_entrenado.predict([caracteristicas])[0]  # Asumiendo que el modelo predice el IMC

# Mostrar el valor del IMC
st.write(f"El IMC predicho es: {prediccion_imc:.2f}")

# Clasificación en función del IMC o riesgo de ACV
if prediccion_imc < 18.5:
    st.write("Peso insuficiente")
elif 18.5 <= prediccion_imc < 24.9:
    st.write("Saludable.")
elif 25 <= prediccion_imc < 29.9:
    st.write("Obesidad.")
else:
    st.write("Obesidad extrema.")
