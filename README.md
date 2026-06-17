# Asistente IA

Asistente de línea de comandos que usa la API de OpenAI para realizar cuatro tareas: traducción de texto, descarga de imágenes, resolución de problemas desde imagen y transcripción de audio.

## Funcionalidades

- **Traducir texto** — traduce cualquier texto al idioma que indiques
- **Descargar imagen desde URL** — descarga y guarda una imagen localmente
- **Resolver problema desde imagen** — analiza un PNG y resuelve el problema que contiene (visión)
- **Transcribir audio** — convierte un archivo de audio a texto con Whisper

## Requisitos

- Python 3.8+
- Cuenta en [OpenAI](https://platform.openai.com) con API key

## Instalación

```bash
git clone https://github.com/1lauraog15-cloud/asistente-ia.git
cd asistente-ia
pip install openai python-dotenv requests
```

Crea un archivo `.env` en la raíz del proyecto:

```
OPENAI_API_KEY=tu_api_key_aquí
```

## Uso

```bash
python asistente.py
```

Se abrirá un menú interactivo donde puedes elegir la función que quieras.
