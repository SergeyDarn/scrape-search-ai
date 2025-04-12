from ai.abstract_llm_runner import AbstractLLMRunner
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class OllamaRunner(AbstractLLMRunner):
    DEFAULT_MODEL = "llama3.2"
    DEFAUL_MODEL_INSTRUCTIONS = (
        "You are tasked with extracting specific information from the following text content: {content}."
        "Please follow these instructions carefully: \n\n"
        "1. **Extract Information:** Only extract the information that directly matches the provided description: {question}."
        "2. **No extra content:** Do not include anny additional text, comments, or explanations in your response."
        "3. **Empty response:** If no information matches the description, return an empty string ('')."
        "4. **Direct data only:** Your output should contain only the data that is explicitly requested, with no other text."
    )

    def __init__(
        self,
        model_name=DEFAULT_MODEL,
        model_instructions=DEFAUL_MODEL_INSTRUCTIONS
    ):
        self.model = OllamaLLM(model=model_name)
        self.model_instructions = model_instructions
        # todo: delete this linesuper().__init__()
    
    
    def ask_ai(self, question: str, content: str) -> str:
        prompt = ChatPromptTemplate.from_template(self.model_instructions)
        chain = prompt | self.model
        
        content_chunks = self.split_content_into_chunks(content)
        parsed_results = []
        
        print(f"Ai is thinking...")
        # todo: add async code to make it run faster
        for i, chunk in enumerate(content_chunks, start=1):
            response = chain.invoke({
                "question": question,
                "content": chunk
            })
            print(f"Ai parsed batch {i} of {len(content_chunks)}")
            parsed_results.append(response)
            
        return "\n".join(parsed_results)