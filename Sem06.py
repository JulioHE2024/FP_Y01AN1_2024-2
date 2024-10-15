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
    for i in range(1, 10):
        st.write(i)
#Ejercicio 3: Tabla de multiplicar
st.subheader("Ejercicio 3: Imprimir la tabla de multiplicar del numero ingresado")
num = st.number_input("Ingrese un numero para ver su tabla de multiplicar del 1 al 12", min_value=1)
if st.button("Ejecutar Ejercicio 3"):
    for i in range (1, 13):
        st.write(f"{num} x {i} = {num*i}")

##########################################################################

#Ejercicio 4: Calcular la media y comparar con 10
st.subheader("Ejercicio 4: Comparar 10 numeros con el valor 10")
numeros_ej1 = st.text_input("Ingresa 10 numeros separados por comas: ", "12, 7, 15, 10, 20, 5, 11, 18, 3, 8")

if st.button("Ejecutar Ejercicio 4"):
    #Convertir la cadena de entrada a una lista de numeros
    lista_numeros = [int(num) for num in numeros_ej1.split(",")]
    media = sum(lista_numeros) / len(lista_numeros)
    mayores = len({num for num in lista_numeros if num > 10})
    iguales = len({num for num in lista_numeros if num == 10})
    menores = len({num for num in lista_numeros if num < 10})

    st.write(f"La media es: {media}")
    st.write(f"Mayores que 10: {mayores}")
    st.write(f"Iguales a 10: {iguales}")
    st.write(f"Menores que 10: {menores}")