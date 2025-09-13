# translator.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env
load_dotenv()

def get_model():
    """Initialize OpenAI chat model using API key from env."""
    return ChatOpenAI(
        model="gpt-4o-mini", 
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")  # ensures key is passed
    )

def translate_text(model, text: str, language: str) -> str:
    """Translate English text into the target language using LangChain prompt template"""
    system_template = "Translate the following from English into {language}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    prompt = prompt_template.invoke({"language": language, "text": text})
    response = model.invoke(prompt)

    return getattr(response, "content", str(response))
