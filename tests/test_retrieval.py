import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(ROOT))

import pytest
from chatbot.retrieval import ChatbotRetrieval

@pytest.fixture
def bot():
    json_path = ROOT / "data" / "contenidos.json"
    return ChatbotRetrieval(path_json=str(json_path))

def test_responder_red_de_datos(bot):
    pregunta = "¿Qué es una red de datos?"
    respuesta = bot.responder(pregunta)
    assert "Una red de datos permite compartir información" in respuesta

def test_responder_protocolos(bot):
    pregunta = "Explícame qué es TCP"
    respuesta = bot.responder(pregunta)
    assert "Transmission Control Protocol" in respuesta or "TCP" in respuesta
