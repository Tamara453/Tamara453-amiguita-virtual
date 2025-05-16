
import streamlit as st

# Colores disponibles
colores = {
    "Rojo": "#FF4B4B",
    "Verde": "#4CAF50",
    "Azul": "#2196F3",
    "Amarillo": "#FFEB3B",
    "Naranja": "#FF9800",
    "Rosa": "#E91E63"
}

st.title("🎨 Aprende los Colores")
st.write("Haz clic en un color:")

# Mostrar botones con los colores
for color, hex_code in colores.items():
    if st.button(color):
        st.markdown(f"<div style='background-color:{hex_code};padding:50px;margin:10px;border-radius:10px'></div>", unsafe_allow_html=True)
        st.success(f"¡Este es el color {color}!")
