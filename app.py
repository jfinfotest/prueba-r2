import requests
import json

url = "https://playground.mockoon.com/users"

try:
    # Realizar la petición GET
    response = requests.get(url)
    
    # Lanzar una excepción si hubo un error HTTP (ej. 404 o 500)
    response.raise_for_status()
    
    # Convertir la respuesta a un diccionario/lista de Python
    data = response.json()
    
    # Imprimir los datos formateados
    print(json.dumps(data, indent=4, ensure_ascii=False))

except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la API: {e}")