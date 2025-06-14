from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from create_taxonomy_documents import create_taxonomy_documents
from app.utils.parse_taxonomy_dmp import parse_names_dmp, parse_nodes_dmp
from dotenv import load_dotenv


load_dotenv()


def load_vector_store():
    
    tax_names = parse_names_dmp("data/ncbi_taxonomy/names.dmp")
    tax_nodes = parse_nodes_dmp("data/ncbi_taxonomy/nodes.dmp")
    
    tax_documents = create_taxonomy_documents(tax_names, tax_nodes)
    
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(tax_documents, embeddings)

    return vectorstore.as_retriever()
