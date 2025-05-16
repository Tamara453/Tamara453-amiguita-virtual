import streamlit as st

st.title("Amiguito Virtual 👧🧒")
st.write("¡Hola Valentina y Luca! Soy tu chatbot amiguito.")

if st.button("Dime hola"):
    st.write("👋 ¡Hola, Valentina y Luca!")

if st.button("Escuchar lo que dices"):
    st.write("🎤 Esta función solo funciona en la app local (con micrófono).")


