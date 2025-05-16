
import streamlit as st
import streamlit.components.v1 as components

# Función para hablar en el navegador
def decir(texto):
    components.html(
        f"""
        <script>
        var mensaje = new SpeechSynthesisUtterance("{texto}");
        window.speechSynthesis.speak(mensaje);
        </script>
        """,
        height=0,
    )

# Título de la app
st.title("🎨 Amiguita Virtual - Colores divertidos")

st.write("¡Haz clic en un botón para decir el color!")

# Botones de colores
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔴 Rojo"):
        decir("Rojo")
        st.write("Has elegido el color rojo.")

with col2:
    if st.button("🟢 Verde"):
        decir("Verde")
        st.write("Has elegido el color verde.")

with col3:
    if st.button("🔵 Azul"):
        decir("Azul")
        st.write("Has elegido el color azul.")
