import chromadb

from ai.db.ai_db_interface import AiDbInterface

class Chroma(AiDbInterface):
    DEFAULT_RESULTS_QTY = 10
    
    def __init__(self, db_location = "./chroma_langchain_db"):
        self.client = chromadb.PersistentClient(
            path=db_location
        )
        
    # todo: add proper typing
    def add_documents(
        self,
        documents,
        metadatas,
        ids,
        collection_name
    ):
        collection = self.get_or_create_collection(collection_name)
        
        collection.add(documents=documents, metadatas=metadatas, ids=ids)
        
    def get_or_create_collection(self, collection_name: str):
        return self.client.get_or_create_collection(name=collection_name)
        
    def get_collection(self, collection_name: str):
        return self.client.get_collection(name=collection_name)
    
    def delete_collection(self, collection_name: str):
        return self.client.delete_collection(name=collection_name)
    
    def query_collection(
        self,
        collection_name: str,
        search_str: str,
        n_results=DEFAULT_RESULTS_QTY
    ):
        print(f"Querying the collection {collection_name}...")
        collection = self.get_or_create_collection(collection_name)

        relevant_results = collection.query(
            query_texts=[search_str],
            n_results=n_results
        )
        
        print("Querying finished")

        return relevant_results