# PROYECTO_FINAL_REDES

Creación de un chatbot en Telegram que actúa como tutor y responde preguntas sobre los fundamentos de la materia Redes de Computadores.

## 📂 Estructura del Proyecto

```bash
proyecto_chatbot_free/
├── data/                   # Contenidos educativos en formato JSON
│   └── contenidos.json
├── chatbot/                # Lógica de recuperación de información
│   ├── __init__.py
│   └── retrieval.py
├── ui/                     # Interfaz del bot en Telegram
│   └── telegram_bot.py
├── tests/                  # Pruebas automatizadas con pytest
│   └── test_retrieval.py
├── .env                    # Variables de entorno (no versionar)
├── .gitignore              # Archivos ignorados por Git
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto (este archivo)
⚙️ Características
🔓 Totalmente gratuito: no depende de servicios de pago ni APIs externas.

🤖 Interfaz Telegram: funciona mediante un bot en Telegram.

📚 Recuperación local: usa TF-IDF (scikit-learn) para encontrar la respuesta más relevante en un JSON de contenidos.

✅ Pruebas: incluye tests con pytest para validar la lógica de recuperación.

🛠 Prerrequisitos
Python 3.8 o superior

Git

(Opcional) virtualenv o herramientas de entornos virtuales

Un bot de Telegram creado mediante BotFather y su token

🚀 Instalación y Configuración
Clonar el repositorio

bash
Copiar
Editar
git clone https://github.com/tu-usuario/PROYECTO_FINAL_REDES.git
cd PROYECTO_FINAL_REDES
Crear y activar entorno virtual (recomendado)

bash
Copiar
Editar
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
Instalar dependencias

bash
Copiar
Editar
pip install -r requirements.txt
Configurar variables de entorno

Crea un archivo .env en la raíz con el siguiente contenido:

ini
Copiar
Editar
TELEGRAM_TOKEN=TU_TOKEN_DE_TELEGRAM
Reemplaza TU_TOKEN_DE_TELEGRAM por el token que obtuviste de BotFather.

Ignorar archivos sensibles

Asegúrate de que .env esté listado en .gitignore para no exponerlo.

🏃‍♂️ Ejecución del Bot
Iniciar el bot

bash
Copiar
Editar
python ui/telegram_bot.py
Verás en consola:

mathematica
Copiar
Editar
Bot de Telegram iniciado. Presiona Ctrl+C para detener.
En Telegram, busca tu bot por su username (p. ej. ChatRedesBot_bot) o visita t.me/ChatRedesBot_bot.

Envía el comando /start y luego pregunta, por ejemplo:

Copiar
Editar
¿Qué es una red de datos?
El bot te responderá con el contenido almacenado en data/contenidos.json.

🧪 Pruebas
Para verificar que la lógica de recuperación funciona correctamente:

bash
Copiar
Editar
pytest -q
