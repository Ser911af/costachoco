import streamlit as st
import requests
import json

# Configuración de la API de LangFlow
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "541622f6-15c2-43ad-a7bf-28014cb6894f"
FLOW_ID = "b4478717-431d-4b38-b48e-fec5142f9757"
APPLICATION_TOKEN = "<AstraCS:ZabHIjbZgYPCUrSkZKlJUSZx:2f6202b20fca202daabb7d1c1e0f00ee76555d1a07bceeaa57737c5814d33e34>"
TWEAKS = {
  "ChatInput-TxwJ9": {},
  "ChatOutput-eI86s": {},
  "Agent-LQsAF": {},
  "Prompt-go8Tr": {}
}

# Función para ejecutar el flujo de LangFlow
def run_flow(message: str, endpoint: str = FLOW_ID, tweaks: dict = TWEAKS) -> dict:
    """
    Envía un mensaje al flujo de LangFlow y devuelve la respuesta.
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": tweaks
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Interfaz de Streamlit
st.title("Chat con el Hotel Costa Choco 🏨")
st.write("¡Bienvenido! Escribe tu mensaje y recibirás una respuesta del asistente del Hotel Costa Choco.")

# Entrada de texto del usuario
user_input = st.text_input("Escribe tu mensaje:")

# Botón para enviar el mensaje
if st.button("Enviar"):
    if user_input:
        # Ejecutar el flujo de LangFlow con el mensaje del usuario
        response = run_flow(user_input)
        
        # Mostrar la respuesta
        if "response" in response:
            st.success(f"Respuesta: {response['response']}")
        else:
            st.error("No se pudo obtener una respuesta válida.")
    else:
        st.warning("Por favor, escribe un mensaje antes de enviar.")