import streamlit as st
import pyttsx3
import speech_recognition as sr
import streamlit as st
import pyttsx3
import speech_recognition as sr

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Función para hablar
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()


# Interfaz de Streamlit
st.title("Chatbot Infantil")
st.write("¡Hola! Soy tu amiguito virtual.")

if st.button('Decir Hola'):
    hablar("¡Hola, Valentina y Luca!")
    st.write("He dicho 'Hola'.")

if st.button('Escuchar lo que dices'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Escuchando...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio)
            st.write(f"Escuché: {texto}")
            hablar(f"Escuché: {texto}")
        except sr.UnknownValueError:
            st.write("No entendí lo que dijiste.")
            hablar("No entendí lo que dijiste.")
            import streamlit as st
import pyttsx3

# Inicializar motor de voz
engine = pyttsx3.init()

# Función para hablar
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Interfaz de usuario
st.title("Amiguito Virtual 👧🧒")
st.write("¡Hola Valentina y Luca! Soy tu chatbot amiguito.")

if st.button("Dime hola"):
    hablar("¡Hola, Valentina y Luca!")
    st.write("👋 He dicho 'Hola'.")

