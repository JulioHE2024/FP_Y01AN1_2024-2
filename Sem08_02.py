import streamlit as st

def calcular(operacion, num1, num2):
    """Realiza la operacion especificada entre num1 y num2"""
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Por favor, ingrese numeros validos"

    if operacion == "Suma":
        return num1+num2
    elif operacion == "Resta":
        return num1-num2
    elif operacion == "Multiplicacion":
        return num1*num2
    elif operacion == "Division":
        if num2 == 0:
            return "Error: No se puede dividir entre 0"
        return num1/num2
    else:
        return "Operacion no valida"
    
def main():
    st.title("CALCULADORA BASICA")
    st.write("Seleccione la operacion e ingrese los numeros:")

    #Seleccione la operacion
    operacion = st.selectbox("Seleccione la operacion:", ("Suma", "Resta", "Multiplicacion", "Division"))

    #Entradas para los numeros
    num1 = st.text_input("Ingrese numero 01:")
    num2 = st.text_input("Ingrese numero 02.")

    #Boton para calcular
    if st.button("Calcular"):
        resultado = calcular(operacion, num1, num2)
        st.write("**El resultado es:**", resultado)

if __name__=="__main__":
    main()


