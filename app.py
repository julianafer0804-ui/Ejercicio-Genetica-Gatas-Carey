import streamlit as st
import numpy as np

# Configuración general
st.set_page_config(page_title="Herencia ligada al sexo - Fenotipo Carey", page_icon="🐱", layout="centered")

st.title("🧬 Herencia ligada al sexo: Fenotipo Carey en gatas 🐈")

st.markdown("""
Este simulador muestra cómo la **inactivación aleatoria del cromosoma X** produce el patrón bicolor característico del 
**fenotipo carey** en gatas heterocigotas para el gen del color del pelaje, ligado al sexo.

El color del pelaje en gatos está determinado por un gen ubicado en el **cromosoma X**:
- 🟨 Alelo `Xᵇ` → color amarillo/anaranjado  
- ⬛ Alelo `Xᴮ` → color negro  

Las hembras con genotipo **XᴮXᵇ** expresan ambos colores en distintas zonas del cuerpo, debido a que en cada célula se **inactiva uno de los dos cromosomas X**, por medio de un mecanismo llamado **compensación de dosis**, este mecanismo en mamíferos garantiza que se sintetice la misma cantidad de producto de genes ligados al cromosoma X en las células de los macho y de las hembras. Qué cromosoma X se inactiva es una cuestión aleatoria que varía de una célula a otra.
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

# Botón para simular
if st.button("Realizar cruzamiento"):
    madre, padre = cruces[cruzamiento]

    st.markdown("### 🔬 Resultado del cruzamiento")
    st.markdown(f"**Genotipos parentales:** {madre} × {padre}")
    st.markdown("**Descendencia posible (hembra heterocigota XᴮXᵇ):**")

    # Generar patrón aleatorio (inactivación X)
    size = 16         # cuadrado más chico
    pixel_size = 18   # píxeles pequeños, pero con espacio entre ellos
    matriz = np.random.choice([0, 1], size=(size, size))

    # Crear cuadrado de píxeles con bordes visibles
    html = f"""
    <div style='
        display: grid;
        grid-template-columns: repeat({size}, {pixel_size}px);
        justify-content: center;
        gap: 2px;
        background-color: #ccc;
        padding: 6px;
        border-radius: 12px;
        width: fit-content;
        margin: auto;
    '>
    """

    for i in range(size):
        for j in range(size):
            color = "#FFD700" if matriz[i, j] == 1 else "#000000"
            html += f"<div style='width:{pixel_size}px; height:{pixel_size}px; background-color:{color}; border-radius:3px;'></div>"
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    st.markdown("""
    Este patrón representa una **inactivación aleatoria del cromosoma X** en una hembra heterocigota XᴮXᵇ.  
    Las células que expresan el alelo `Xᴮ` producen pigmento negro, mientras que las que expresan `Xᵇ` producen color amarillo/anaranjado.
    """)
else:
    st.info("Seleccioná un cruzamiento y presioná **Realizar cruzamiento** para generar el patrón del fenotipo carey.")
