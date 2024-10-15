import streamlit as st

#titulo de la aplicacion
st.title("Ejercicios con bucles basicos en python")

#Ejercicio 1: Imprimir 10 veces 'Hola Mundo'
st.subheader("Ejercicio 1: Imprimir 'Hola Mundo' 10 veces")
if st.button("Ejecutar Ejercicio 1"):
    for i in range(10):
        st.write("Hola Mundo")
#Ejercicio 2: Imprimir los primeros 10 numeros
st.subheader("Ejercicio 2: Imprimir los 10 primeros numeros")
if st.button("Ejecutar Ejercicio 2"):
    for u in range(1, 10):
        st.write(i)   