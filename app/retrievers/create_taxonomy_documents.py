from langchain_core.documents import Document
from typing import Any, List

def create_taxonomy_documents(names: dict[str, dict[str, Any]], nodes: dict[str, dict[str, str]]):
    documents: List[Document] = []
    
    for tax_id, name_data in names.items():
        if tax_id not in nodes:
            continue
        
        scientific_name = name_data.get("scientific_name", "[unknown]")
        synonyms = ", ".join(name_data.get("synonyms", []))
        rank = nodes[tax_id]["rank"]
        parent_id = nodes[tax_id]["parent"]
        
        text = f"{scientific_name} (TaxID: {tax_id}) is a {rank}."
        if synonyms:
            text += f" Synonyms: {synonyms}."
        text += f" Parent TaxID: {parent_id}."
        
        document = Document(
            page_content=text,
            metadata={
                "tax_id": int(tax_id),
                "rank": rank,
                "parent_tax_id": int(parent_id)
            }
        )
        
        documents.append(document)
        
    return documents
