from ai.chroma import Chroma
from langchain_core.documents import Document

# todo: separate db and llm runners into separate folders (add subfolders)
class AiDb:
    def __init__(self):
        self.db = Chroma()

    # todo: type properly, and maybe move this logic to Chroma class?
    def add_documents(self, site_name, content_array):
        documents = []
        metadatas = []
        ids = []
        
        for i, content_item in enumerate(content_array):
            id = str(i)
            document = content_item["title"] + " " + content_item["content"]
            metadata={"url": content_item["url"]}
            
            documents.append(document)
            metadatas.append(metadata)
            ids.append(id)

        self.db.add_documents(documents, metadatas, ids, site_name)
        
    def get_collection(self, collection_name: str):
        return self.db.get_collection(collection_name)
    
    def query_collection(
        self,
        collection_name: str,
        search_str: str,
        n_results: int
    ):
        return self.db.query_collection(collection_name, search_str, n_results)