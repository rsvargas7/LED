import streamlit as st
import serial
import time

# Cambia el puerto COM por el que te muestre tu sistema (ej. COM3, /dev/ttyUSB0, etc.)
ARDUINO_PORT = 'COM3'  # Ajusta esto a tu puerto
BAUD_RATE = 9600

@st.cache_resource
def get_serial_connection():
    try:
        return serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    except:
        st.error("No se pudo conectar al Arduino.")
        return None

arduino = get_serial_connection()

st.title("Control de LED con Streamlit y Arduino")

if st.button("Encender LED"):
    if arduino:
        arduino.write(b'1')
        st.success("LED Encendido")

if st.button("Apagar LED"):
    if arduino:
        arduino.write(b'0')
        st.success("LED Apagado")
