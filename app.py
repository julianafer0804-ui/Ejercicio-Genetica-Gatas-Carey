import streamlit as st
import numpy as np

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Herencia ligada al sexo: Gato Carey",
    page_icon="🐱",
    layout="centered"
)

st.title("🐾 Herencia ligada al sexo: Gato Carey 🧬")
st.write("Visualización interactiva de la **inactivación del cromosoma X** en gatas tricolores (carey).")

# --- MOSTRAR GENOTIPOS ---
col1, col2, col3 = st.columns([1, 0.3, 1])
with col1:
    st.markdown("<div style='display:flex;align-items:center;gap:8px;'>🟨<b>bb</b></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div style='font-size:20px;text-align:center;'>×</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div style='display:flex;align-items:center;gap:8px;'>⬛<b>BB</b></div>", unsafe_allow_html=True)

# --- GENERAR Y MOSTRAR EL PATRÓN ---
def generar_patron_html():
    colores = np.random.choice(["#000000", "#FFD700"], size=(10, 10))
    html = "<div style='display:grid;grid-template-columns:repeat(10,20px);gap:1px;background:#ccc;padding:5px;border-radius:10px;'>"
    for fila in colores:
        for color in fila:
            html += f"<div style='width:20px;height:20px;background:{color};border-radius:3px;'></div>"
    html += "</div>"
    return html

if st.button("Realizar cruzamiento 🔄") or "patron" not in st.session_state:
    st.session_state["patron"] = generar_patron_html()

st.markdown(st.session_state["patron"], unsafe_allow_html=True)

# --- EXPLICACIÓN BIOLÓGICA ---
st.markdown("""
### 🧬 Explicación biológica

En las gatas “carey” (**XᴮXᵇ**), el gen del color del pelaje se encuentra en el **cromosoma X**.  
Durante el desarrollo embrionario, uno de los cromosomas X se **inactiva al azar** en cada célula, un fenómeno conocido como **inactivación del cromosoma X**.

Esto genera un mosaico de células que expresan:
- el alelo **B (negro)**  
- o el alelo **b (amarillo)**  

El resultado es el **patrón tricolor característico** del pelaje “carey”, un ejemplo visual de **compensación de dosis** en mamíferos.
""")
