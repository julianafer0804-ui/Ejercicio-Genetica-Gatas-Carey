import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

# --- BOTÓN PARA GENERAR NUEVO PATRÓN ---
if st.button("Realizar cruzamiento 🔄"):
    st.session_state["pattern"] = np.random.choice(["black", "gold"], size=(10, 10))
elif "pattern" not in st.session_state:
    st.session_state["pattern"] = np.random.choice(["black", "gold"], size=(10, 10))

pattern = st.session_state["pattern"]

# --- MOSTRAR EL PATRÓN ---
fig, ax = plt.subplots(figsize=(4, 4))
for i in range(10):
    for j in range(10):
        color = pattern[i, j]
        ax.add_patch(plt.Rectangle((j, 9 - i), 1, 1, color=color))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

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
