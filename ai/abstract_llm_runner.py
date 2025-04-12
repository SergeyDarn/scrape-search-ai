from typing import List

class AbstractLLMRunner:
    SAFE_CONENT_CHUNK_SIZE = 6000
    
    def __init__(self):
        pass

    def ask_ai(self, question: str, content: str) -> str:
        pass
    
    def split_content_into_chunks(
        self,
        content: str,
        max_length: int = SAFE_CONENT_CHUNK_SIZE
    ) -> List[str]:
        return [
            # todo: figure out how this works
            content[i: i + max_length] for i in range(0, len(content), max_length)
        ]