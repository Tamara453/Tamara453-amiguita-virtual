import streamlit as st
import pyttsx3

# Inicializar motor de voz
engine = pyttsx3.init()

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

st.title("Amiguito Virtual 👧🧒")
st.write("¡Hola Valentina y Luca! Soy tu chatbot amiguito.")

# Botón para decir hola
if st.button("Dime hola"):
    hablar("¡Hola, Valentina y Luca!")
    st.write("👋 He dicho 'Hola'.")

# Diccionario de cuentos
cuentos = {
    "Conejito Coco": """Había una vez un conejito llamado Coco.
Coco amaba saltar y jugar en el bosque con sus amigos.
Un día, encontró una zanahoria mágica que le dio poderes para correr muy rápido.""",

    "La Estrella Brillante": """En el cielo, una pequeña estrella quería brillar más que todas.
Cada noche, hacía un deseo y finalmente su luz iluminó toda la noche.""",

    "El Pez Dorado": """Un pez dorado nadaba feliz en el río.
Un día, ayudó a un niño perdido a encontrar el camino a casa."""
}

st.write("Elige un cuento para escuchar:")

# Botones para cada cuento
for titulo, texto in cuentos.items():
    if st.button(titulo):
        st.write(texto)
        hablar(texto)

