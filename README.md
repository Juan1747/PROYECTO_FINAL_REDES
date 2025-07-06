# PROYECTO\_FINAL\_REDES

Creación de un chatbot en Telegram que actúa como tutor y responde preguntas sobre los fundamentos de Redes de Computadores.

## Índice

* [Estructura del proyecto](#estructura-del-proyecto)
* [Requisitos](#requisitos)
* [Instalación](#instalación)
* [Configuración](#configuración)
* [Uso](#uso)
* [Pruebas](#pruebas)
* [Extensiones futuras](#extensiones-futuras)

## Estructura del proyecto

```text
proyecto_chatbot_free/
├── data/                # Contenidos educativos en JSON
│   └── contenidos.json
├── chatbot/             # Lógica de recuperación de información
│   ├── __init__.py
│   └── retrieval.py
├── ui/                  # Interfaz del bot en Telegram
│   └── telegram_bot.py
├── tests/               # Pruebas automatizadas con pytest
│   └── test_retrieval.py
├── .env                 # Variables de entorno (no versionar)
├── .gitignore           # Archivos ignorados por Git
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación del proyecto (este archivo)
```

## Requisitos

* Python 3.8 o superior
* Git
* (Opcional) Entorno virtual con `venv` o `virtualenv`
* Cuenta de Telegram y un bot creado con BotFather

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/PROYECTO_FINAL_REDES.git
   cd PROYECTO_FINAL_REDES
   ```
2. (Opcional) Crea y activa un entorno virtual:

   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```
3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. En la raíz del proyecto, crea un archivo `.env`:

   ```ini
   TELEGRAM_TOKEN=TU_TOKEN_DE_TELEGRAM
   ```
2. Reemplaza `TU_TOKEN_DE_TELEGRAM` por el token que BotFather te proporcionó.
3. Verifica que `.env` esté listado en `.gitignore` para no subirlo a GitHub.

## Uso

Para iniciar el bot, ejecuta:

```bash
python ui/telegram_bot.py
```

En la consola verás:

```
Bot de Telegram iniciado. Presiona Ctrl+C para detener.
```

Luego, en Telegram:

1. Busca tu bot por su username (p.ej. `ChatRedesBot_bot`).
2. Envía el comando `/start`.
3. Formula preguntas, por ejemplo:

   ```text
   ¿Qué es una red de datos?
   ```
4. El bot responderá con contenido extraído de `data/contenidos.json`.

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest -q
```

Deberías ver:

```
. .
2 passed
```

## Extensiones futuras

* Añadir más módulos educativos al archivo JSON.
* Desplegar una interfaz web (Gradio) para el chatbot.
* Integrar un modelo de lenguaje local para respuestas más flexibles.
* Implementar métricas de uso y logging de preguntas frecuentes.
