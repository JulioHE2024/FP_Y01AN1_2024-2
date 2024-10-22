import streamlit as st 

def mostrar_menu():
    st.title("Ejemplo de Menu")
    st.write("Selecciona una opcion del menu")

    menu = ["Archivo", "Editar", "Ver", "Salir"]
    seleccion = ""

    while seleccion != "Salir":
        seleccion = st.radio ("Menú", menu)

        if seleccion == "Archivo":
            st.write("Seleccionaste: Archivo")
        elif seleccion == "Editar":
            st.write("Seleccionaste: Editar")
        elif seleccion == "Ver":
            st.write("Seleccionaste: Ver")
        elif seleccion == "Salir":
            st.write("¡Saliendo del Menú!")
            break

if__name___=="__main__"