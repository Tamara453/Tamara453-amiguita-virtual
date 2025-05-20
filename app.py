
import streamlit as st

# Función para mostrar cuentos
def mostrar_cuento(titulo, contenido):
    st.subheader(titulo)
    st.write(contenido)

# Interfaz principal
st.title("📚 Amiguita Virtual - Cuentos Cortitos")
st.write("¡Hola Valentina y Luca! Elige un cuento para leer:")

# Botones de colores para cuentos
col1, col2 = st.columns(2)

with col1:
    if st.button("🐰 El conejito curioso"):
        mostrar_cuento("🐰 El conejito curioso", 
        "Había una vez un conejito que quería saber todo. Saltaba y preguntaba a todos los animales. Al final, encontró a su mamá que le dijo: '¡Saber es bonito, pero descansar también!'")

    if st.button("🐢 La tortuga lenta"):
        mostrar_cuento("🐢 La tortuga lenta", 
        "Una tortuga iba despacito, pero siempre avanzaba. Un día, todos vieron que había llegado muy lejos. '¡Qué bien lo haces!', dijeron. 'Pasito a pasito', respondió la tortuga.")

with col2:
    if st.button("🐶 El perrito valiente"):
        mostrar_cuento("🐶 El perrito valiente", 
        "Un perrito escuchó un ruido en la noche. Se acercó despacito y... ¡era solo una rana! El perrito rió y volvió feliz a su cama.")

    if st.button("🦊 La zorrita y la estrella"):
        mostrar_cuento("🦊 La zorrita y la estrella", 
        "Una noche, una estrella cayó cerca de una zorrita. Ella la cuidó con cariño, y cuando volvió al cielo, brilló más fuerte por su nueva amiga.")

# Pie de página
st.markdown("---")
st.markdown("👧🧒 Cuentos para Valentina y Luca con mucho cariño.")



