import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class ChatbotRetrieval:
    def __init__(self, path_json: str = "data/contenidos.json"):
        # Carga los módulos desde el JSON
        data_path = Path(path_json)
        if not data_path.exists():
            raise FileNotFoundError(f"No se encontró el archivo {path_json}")

        with data_path.open(encoding="utf-8") as f:
            payload = json.load(f)
        self.modulos = payload.get("modulos", [])
        self.textos = [m["contenido"] for m in self.modulos]

        # Entrena el vectorizador TF-IDF (sin stop_words explícito)
        self.vectorizer = TfidfVectorizer()  
        self.tfidf_matrix = self.vectorizer.fit_transform(self.textos)

    def responder(self, pregunta: str, top_k: int = 1) -> str:
        """
        Devuelve el texto de los top_k módulos más relevantes
        según la similitud con la pregunta.
        """
        query_vec = self.vectorizer.transform([pregunta])
        sims = linear_kernel(query_vec, self.tfidf_matrix).flatten()
        idxs = sims.argsort()[-top_k:][::-1]
        return "\n\n".join(self.textos[i] for i in idxs)
