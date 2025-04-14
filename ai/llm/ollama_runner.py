from ai.llm.abstract_llm_runner import AbstractLLMRunner
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

from multiprocessing import Pool
from functools import partial
from typing import List
import time

class OllamaRunner(AbstractLLMRunner):
    # todo: move default olama model to .env config
    DEFAULT_MODEL = "llama3" # llama3.2 - smaller model, llama3 - more accurate and demanding
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
    
    
    def ask_ai(self, question: str, context: List[str]) -> str:
        prompt = ChatPromptTemplate.from_template(self.model_instructions) 
        chain = prompt | self.model
        
        content_chunks = self.split_content_into_chunks(context)

        time1 = time.perf_counter()
        print(f"Ai is thinking: {question}")

        parsed_results = []
        
        for i, chunk in enumerate(content_chunks, start=1):
            response = chain.invoke({
                "question": question,
                "content": chunk
            })
            parsed_results.append(response)

            percentage = int(i / len(content_chunks) * 100)
            print(f"Ai is thinking... {percentage}% (batch {i}/{len(content_chunks)})")
            
        print(f"Querying finished in {time.perf_counter() - time1}")
            
        return "\n".join(parsed_results)