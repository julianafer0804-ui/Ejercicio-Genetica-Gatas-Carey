import streamlit as st
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Herencia ligada al sexo - Fenotipo Carey", page_icon="🐱", layout="centered")

st.title("🐾 Herencia ligada al sexo: Fenotipo Carey (Tortoiseshell)")

st.markdown("""
Este simulador muestra cómo la **inactivación aleatoria del cromosoma X** genera el patrón bicolor característico del 
**fenotipo carey** en gatas heterocigotas para el gen del color, ligado al sexo.

El color del pelaje en gatos está determinado por un gen ubicado en el **cromosoma X**:
- 🟨 Alelo `Xᵇ` → color amarillo/anaranjado  
- ⬛ Alelo `Xᴮ` → color negro  

Las hembras con genotipo **XᴮXᵇ** expresan ambos colores en distintas zonas del cuerpo, debido a que en cada célula se **inactiva uno de los dos cromosomas X**.
""")

st.divider()

# Opciones de cruzamiento posibles
cruces = {
    "🟨 XᵇXᵇ × ⬛ XᴮY": ("XᵇXᵇ", "XᴮY"),
    "⬛ XᴮXᴮ × 🟨 XᵇY": ("XᴮXᴮ", "XᵇY")
}

# Selector de cruzamiento
cruzamiento = st.selectbox(
    "Seleccioná un cruzamiento posible:",
    options=list(cruces.keys())
)

# Botón de simulación
if st.button("Realizar cruzamiento"):
    st.markdown("### 🔬 Resultado del cruzamiento")
    madre, padre = cruces[cruzamiento]
    st.markdown(f"**Genotipos parentales:** {madre} × {padre}")

    # Generar mosaico aleatorio (inactivación X)
    size = 20
    matriz = np.random.choice(["🟨", "⬛"], size=(size, size))
    pattern = "".join("".join(row) + "\n" for row in matriz)

    st.text(pattern)

    st.markdown("""
    Cada mosaico representa un patrón posible de **inactivación aleatoria del cromosoma X** en una hembra heterocigota (XᴮXᵇ).  
    Las células que expresan el alelo `Xᴮ` producen pigmento negro (⬛), mientras que las que expresan `Xᵇ` producen color amarillo (🟨).
    """)

else:
    st.info("Seleccioná un cruzamiento y presioná **Realizar cruzamiento** para generar el patrón del fenotipo carey.")
