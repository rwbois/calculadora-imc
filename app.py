import streamlit as st

st.set_page_config(page_title="Calculadora de IMC Pro", page_icon="⚖️")

st.title("⚖️ Calculadora de IMC y Peso Objetivo")

# Entradas del usuario
col1, col2 = st.columns(2)
with col1:
    peso = st.number_input("Tu peso actual (kg):", min_value=10.0, max_value=300.0, value=70.0)
with col2:
    altura = st.number_input("Tu altura (metros):", min_value=0.5, max_value=2.5, value=1.70)

if st.button("Analizar mi composición"):
    imc_actual = peso / (altura ** 2)
    
    # Rango de peso saludable
    peso_min = 18.5 * (altura ** 2)
    peso_max = 24.9 * (altura ** 2)
    
    st.divider()
    
    # Mostrar resultado principal con una métrica visual
    st.metric(label="Tu IMC Actual", value=f"{imc_actual:.1f}")

    # Lógica de estados y recomendaciones
    if imc_actual < 18.5:
        faltante = peso_min - peso
        st.warning(f"Clasificación: **Bajo peso**. Te faltan aproximadamente **{faltante:.1f} kg** para alcanzar un peso saludable.")
    elif 18.5 <= imc_actual <= 24.9:
        st.success("Clasificación: **Peso saludable**. ¡Mantente así!")
    elif 25.0 <= imc_actual <= 29.9:
        sobrante = peso - peso_max
        st.info(f"Clasificación: **Sobrepeso**. Estás aproximadamente **{sobrante:.1f} kg** por encima del rango ideal.")
    else:
        sobrante = peso - peso_max
        st.error(f"Clasificación: **Obesidad**. Estás aproximadamente **{sobrante:.1f} kg** por encima del rango ideal.")

    # Expansor con detalles técnicos
    with st.expander("Ver tabla de rangos"):
        st.write("""
        * **Bajo peso:** < 18.5
        * **Peso normal:** 18.5 – 24.9
        * **Sobrepeso:** 25.0 – 29.9
        * **Obesidad:** > 30.0
        """)

# --- PIE DE PÁGINA (Tu aclaración) ---
st.divider()
st.caption("⚠️ **Nota importante:**")
st.caption("El IMC es una métrica útil pero limitada. No diferencia entre músculo y grasa (un atleta puede tener un IMC de 'sobrepeso' siendo pura fibra). Es una excelente guía general, pero no reemplaza el ojo clínico de un profesional de la salud.")