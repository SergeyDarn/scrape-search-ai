from typing import List

class AbstractLLMRunner:
    SAFE_CONTENT_CHUNK_SIZE = 6000
    
    def __init__(self):
        pass

    def ask_ai(self, question: str, content: str) -> str:
        pass
    
    def split_content_into_chunks(
        self,
        content: List[str],
        chunk_size: int = SAFE_CONTENT_CHUNK_SIZE
    ) -> List[str]:
        chunks = [];
        
        for chunk in content:
            split_chunks = [
                chunk[i: i + chunk_size] for i in range(0, len(chunk), chunk_size)
            ]
            chunks += split_chunks
            
        return chunks