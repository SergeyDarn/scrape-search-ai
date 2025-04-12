from ai.ollama_runner import OllamaRunner

# todo - figure out how to install Ollama for user

llm_runner = OllamaRunner()

def ask_ai(question: str, content: str) -> str:
    return llm_runner.ask_ai(question, content)