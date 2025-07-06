import os
import sys
from pathlib import Path
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# 1) Añadir la raíz del proyecto al path para importar chatbot
ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

# 2) Cargar variables de entorno
load_dotenv(dotenv_path=ROOT / ".env")
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("Falta TELEGRAM_TOKEN en el archivo .env")

# 3) Importar la lógica de recuperación
from chatbot.retrieval import ChatbotRetrieval
bot_logic = ChatbotRetrieval(path_json=str(ROOT / "data" / "contenidos.json"))

# 4) Handlers async
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! 🤖\n"
        "Soy tu asistente de Redes de Computadores.\n"
        "Envíame cualquier pregunta y te responderé."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pregunta = update.message.text
    respuesta = bot_logic.responder(pregunta)
    await update.message.reply_text(respuesta)

# 5) Punto de entrada
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    )

    print("Bot de Telegram iniciado. Presiona Ctrl+C para detener.")
    app.run_polling()

if __name__ == "__main__":
    main()
