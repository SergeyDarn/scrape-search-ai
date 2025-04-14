from ai.llm.ollama_runner import OllamaRunner
from typing import List
# todo - figure out how to install Ollama for user

# todo: ? move inside function
llm_runner = OllamaRunner()

def ask_ai(question: str, context: List[str]) -> str:
    return llm_runner.ask_ai(question, context)