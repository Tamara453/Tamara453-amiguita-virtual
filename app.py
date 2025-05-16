import streamlit as st

# Estilos CSS para colores y tamaño
st.markdown("""
<style>
body {
    background-color: #FFF8DC;
    color: #333333;
}
h1, h3 {
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.stButton>button {
    background-color: #FFA07A;
    color: white;
    height: 3em;
    width: 100%;
    font-size: 1.2em;
    border-radius: 10px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("Amiguito Virtual 👧🧒")
st.write("¡Hola Valentina y Luca! Escoge un cuento y yo te lo leeré.")

# Cuentos con imágenes (URL)
cuentos = {
    "El Gatito Misi": {
        "texto": [
            "Érase una vez un gatito llamado Misi.",
            "Misi tenía mucho miedo de la oscuridad.",
            "Pero una noche, una luciérnaga le hizo compañía.",
            "Desde entonces, Misi no tuvo miedo jamás.",
            "¡Fin!"
        ],
        "imagen": "https://cdn.pixabay.com/photo/2016/02/18/18/38/cat-1209336_960_720.jpg"
    },
    "La Tortuga y la Liebre": {
        "texto": [
            "Había una vez una liebre muy rápida y una tortuga muy lenta.",
            "La liebre se burlaba de la tortuga por ser tan lenta.",
            "La tortuga retó a la liebre a una carrera.",
            "Aunque la liebre corría rápido, se quedó dormida.",
            "La tortuga ganó la carrera con paciencia.",
            "¡Fin!"
        ],
        "imagen": "https://cdn.pixabay.com/photo/2017/06/20/21/17/turtle-2429889_960_720.jpg"
    }
}

# Selector de cuento
cuento_elegido = st.selectbox("Selecciona un cuento", list(cuentos.keys()))

# Mostrar imagen del cuento
st.image(cuentos[cuento_elegido]["imagen"], width=400)

# Estado para índice
if 'index' not in st.session_state:
    st.session_state.index = 0

if 'cuento_actual' not in st.session_state:
    st.session_state.cuento_actual = cuento_elegido

if st.session_state.cuento_actual != cuento_elegido:
    st.session_state.index = 0
    st.session_state.cuento_actual = cuento_elegido

# Mostrar texto actual
frase = cuentos[cuento_elegido]["texto"][st.session_state.index]
st.markdown(f"<h3>{frase}</h3>", unsafe_allow_html=True)

# Botones coloridos para navegar
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Anterior") and st.session_state.index > 0:
        st.session_state.index -= 1

with col2:
    if st.button("Siguiente ➡️") and st.session_state.index < len(cuentos[cuento_elegido]["texto"]) - 1:
        st.session_state.index += 1

# Lectura automática con JS
js = f"""
<script>
const utterance = new SpeechSynthesisUtterance("{frase}");
speechSynthesis.cancel();
speechSynthesis.speak(utterance);
</script>
"""

st.components.v1.html(js)


