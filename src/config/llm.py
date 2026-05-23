from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()  # Carga variables desde .env si existe
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        google_api_key=GEMINI_API_KEY,
        temperature=0.2
    )

def create_routing_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=GEMINI_API_KEY,
        temperature=0.0
    )

def create_synthesizer_llm(): # Para el Synthesizer y el maintenance agent, queremos un modelo que sea bueno generando texto coherente y amigable, pero no necesitamos la última versión. Además, un modelo más ligero puede ser más rápido y suficiente para esta tarea.    
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=GEMINI_API_KEY,
        temperature=0.4
    )

