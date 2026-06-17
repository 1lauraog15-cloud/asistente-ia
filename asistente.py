import os
import json
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. TRADUCCIÓN TEXTO
def traducir_texto():
    print("\n--- TRADUCCIÓN DE TEXTO ---")
    texto = input("Ingresa el texto a traducir: ")
    idioma = input("Idioma destino (ej: inglés, francés, alemán): ")
    
    datos = json.dumps({"texto": texto, "idioma": idioma})
    
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"Traduce el siguiente JSON al idioma indicado y devuelve solo la traducción: {datos}"
        }]
    )
    print("\nTraducción:", respuesta.choices[0].message.content)

# 2. DESCARGA IMAGEN DESDE URL
def descargar_imagen():
    print("\n--- DESCARGA DE IMAGEN ---")
    url = input("Ingresa la URL de la imagen: ")
    nombre = input("Nombre para guardar el archivo (ej: imagen.jpg): ")
    
    respuesta = requests.get(url)
    with open(nombre, "wb") as f:
        f.write(respuesta.content)
    print(f"\nImagen guardada como: {nombre}")

# 3. RESOLUCIÓN PROBLEMA DESDE IMAGEN
def resolver_imagen():
    print("\n--- RESOLVER PROBLEMA DESDE IMAGEN ---")
    ruta = input("Ingresa la ruta del archivo PNG (ej: problema.png): ")
    
    with open(ruta, "rb") as f:
        import base64
        imagen_base64 = base64.b64encode(f.read()).decode("utf-8")
    
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": "Resuelve el problema que aparece en esta imagen."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{imagen_base64}"}}
            ]
        }]
    )
    print("\nRespuesta:", respuesta.choices[0].message.content)

# 4. TRANSCRIPCIÓN AUDIO
def transcribir_audio():
    print("\n--- TRANSCRIPCIÓN DE AUDIO ---")
    ruta = input("Ingresa la ruta del archivo de audio (ej: audio.mp3): ")
    
    with open(ruta, "rb") as f:
        transcripcion = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    print("\nTranscripción:", transcripcion.text)

# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n=============================")
        print("     ASISTENTE IA - MENÚ     ")
        print("=============================")
        print("1. Traducir texto")
        print("2. Descargar imagen desde URL")
        print("3. Resolver problema desde imagen")
        print("4. Transcribir audio")
        print("5. Salir")
        
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "1":
            traducir_texto()
        elif opcion == "2":
            descargar_imagen()
        elif opcion == "3":
            resolver_imagen()
        elif opcion == "4":
            transcribir_audio()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()