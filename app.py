
import streamlit as st

# Títulos y bienvenida
st.title("Amiguito Virtual 👧🧒")
st.write("¡Hola Valentina y Luca! Escoge un cuento y yo te lo leeré.")

# Definir cuentos
cuentos = {
    "El Gatito Misi": [
        "Érase una vez un gatito llamado Misi.",
        "Misi tenía mucho miedo de la oscuridad.",
        "Pero una noche, una luciérnaga le hizo compañía.",
        "Desde entonces, Misi no tuvo miedo jamás.",
        "¡Fin!"
    ],
    "La Tortuga y la Liebre": [
        "Había una vez una liebre muy rápida y una tortuga muy lenta.",
        "La liebre se burlaba de la tortuga por ser tan lenta.",
        "La tortuga retó a la liebre a una carrera.",
        "Aunque la liebre corría rápido, se quedó dormida.",
        "La tortuga ganó la carrera con paciencia.",
        "¡Fin!"
    ]
}

# Selector de cuento
cuento_elegido = st.selectbox("Selecciona un cuento", list(cuentos.keys()))

# Guardar índice en sesión para navegar
if 'index' not in st.session_state:
    st.session_state.index = 0

# Resetear índice si cambia el cuento
if 'cuento_actual' not in st.session_state:
    st.session_state.cuento_actual = cuento_elegido

if st.session_state.cuento_actual != cuento_elegido:
    st.session_state.index = 0
    st.session_state.cuento_actual = cuento_elegido

# Mostrar la frase actual
frase = cuentos[cuento_elegido][st.session_state.index]
st.markdown(f"<h3>{frase}</h3>", unsafe_allow_html=True)

# Botones para avanzar y retroceder
col1, col2 = st.columns(2)

with col1:
    if st.button("Anterior") and st.session_state.index > 0:
        st.session_state.index -= 1

with col2:
    if st.button("Siguiente") and st.session_state.index < len(cuentos[cuento_elegido]) - 1:
        st.session_state.index += 1

# Código para lectura automática con JS
js = f"""
<script>
const utterance = new SpeechSynthesisUtterance("{frase}");
speechSynthesis.cancel();
speechSynthesis.speak(utterance);
</script>
"""

st.components.v1.html(js)

