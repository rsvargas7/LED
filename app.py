import streamlit as st
import paho.mqtt.client as mqtt

# Configuración del Broker MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "led/control"

# Conectar al broker MQTT
client = mqtt.Client()
client.connect(BROKER, PORT, 60)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        st.success("Conectado al broker MQTT")
    else:
        st.error("Error al conectar al broker MQTT")

# Asignar la función de conexión
client.on_connect = on_connect

# Conectar al broker
client.loop_start()

# Interfaz de Streamlit
st.title("Control de LED con MQTT")

# Switch (checkbox) para controlar el LED
led_on = st.checkbox("Encender LED", value=False)

# Enviar comando al Arduino (Wokwi o físico) dependiendo del estado del switch
if led_on:
    client.publish(TOPIC, "on")
    st.success("LED Encendido")
else:
    client.publish(TOPIC, "off")
    st.success("LED Apagado")

# Mantener la conexión MQTT activa
client.loop_forever()
