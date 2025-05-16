import streamlit as st

st.title("Amiguito Virtual 👧🧒")
st.write("¡Hola Valentina y Luca! Vamos a leer un cuento cortito.")

# Lista de frases del cuento
cuento = [
    "Érase una vez un gatito llamado Misi.",
    "Misi tenía mucho miedo de la oscuridad.",
    "Pero una noche, una luciérnaga le hizo compañía.",
    "Desde entonces, Misi no tuvo miedo jamás.",
    "¡Fin!"
]

# Guardar el índice actual en sesión para avanzar
if 'index' not in st.session_state:
    st.session_state.index = 0

# Mostrar la frase actual
st.write(cuento[st.session_state.index])

# Botones para avanzar o retroceder
if st.button('Siguiente'):
    if st.session_state.index < len(cuento) - 1:
        st.session_state.index += 1

if st.button('Anterior'):
    if st.session_state.index > 0:
        st.session_state.index -= 1

