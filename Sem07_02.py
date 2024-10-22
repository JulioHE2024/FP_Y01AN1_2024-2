import streamlit as st 

#Funcion principal para verificar automoviles
def verificar_automoviles():
    st.title("Centro de Verificacion de Automoviles")

    #Lista para almacenar los puntos  contaminantes
    if 'puntos_contaminantes' not in st.session_state:
        st.session_state.puntos_contaminantes = []

    #Input para los puntos contaminantes del automovil
    puntos = st.number_input("Ingrese los puntos contaminantes del automovil", min_value=0.0, step=0.1)

    #Boton para registrar el automovil 
    if st.button("Registrar automovil"):
        st.session_state.puntos_contaminantes.append(puntos)
        st.success(f"Automovil registrado con {puntos} puntos contaminantes.")

    #Mostrar los datos registrados hasta el momento
    if len(st.session_state.puntos_contaminantes) > 0 and st.button("Calcular resultados"):
        promedio = sum(st.session_state.puntos_contaminantes) / len(st.session_state.puntos_contaminantes)
        menos_contaminacion = min(st.session_state.puntos_contaminantes)
        mas_contaminacion = max(st.session_state.puntos_contaminantes)

        #Mostrar los resultados
        st.write(f"Promedio de puntos contaminantes: {promedio: 2f}")
        st.write(f"El automovil que menos contamino tiene {menos_contaminacion: 2f}")
        st.write(f"El automovil que mas contamino tiene {mas_contaminacion: 2f}")

    #Mostrar para reiniciar los datos
    if st.button("Reiniciar Datos"):
        se.session_state.puntos_contaminantes = []
        st.success("Datos reiniciados correctamemte")
    
#Ejecutar la funcion
if __name__=="__main__":
    verificar_automoviles()



