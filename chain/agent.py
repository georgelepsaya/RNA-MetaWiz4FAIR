import json
import requests
import os
from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()


class RNAMetadataAgent:
    def __init__(self, temperature: float = 0.2, model: str = "gpt-3.5-turbo"):
        self.llm = ChatOpenAI(temperature=temperature, model=model, api_key=os.getenv("OPENAI_API_KEY"))
        self.tools = [self._create_ncbi_tool()]
        self.agent_executor = self._create_agent()
    
    @staticmethod
    def _create_ncbi_tool():
        @tool
        def search_ncbi_taxonomy(query: str) -> str:
            """
            Search NCBI taxonomy database for organism IDs based on a partial or full organism name.
            
            Args:
                query: Partial or full taxonomic name to search for
                
            Returns:
                JSON string with taxonomy suggestions including IDs and names
            """
            api_key = os.getenv("NCBI_API_KEY", "")
            
            url = "https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon_suggest"
            headers = {
                "accept": "application/json",
                "Content-Type": "application/json"
            }
            if api_key:
                headers["api-key"] = api_key
                
            payload = {"taxon_query": query}
            
            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                if "sci_name_and_ids" in data and data["sci_name_and_ids"]:
                    results = []
                    for item in data["sci_name_and_ids"][:5]:
                        result = {
                            "tax_id": item.get("tax_id", ""),
                            "scientific_name": item.get("sci_name", ""),
                            "common_name": item.get("common_name", ""),
                            "rank": item.get("rank", ""),
                            "matched_term": item.get("matched_term", "")
                        }
                        results.append(result)
                    return json.dumps(results, indent=2)
                else:
                    return json.dumps({"message": "No results found for the given query"})
                    
            except requests.exceptions.RequestException as e:
                return json.dumps({"error": f"Failed to query NCBI API: {str(e)}"})
        
        return search_ncbi_taxonomy
    
    def _create_agent(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system",
             """You are an RNA-seq metadata assistant helping users fill in metadata fields.

                Current metadata context:
                {context}

                When users ask about organism IDs:
                1. Mention that you used the NCBI Taxonomy API.
                1. Use the search_ncbi_taxonomy tool to find matching organisms
                2. Present the results clearly, showing both the scientific name and tax_id
                3. List all found organisms with all of fields from the response
                4. After that, recommend the most appropriate match based on the user's query
                5. Explain why you're recommending a particular ID
            """),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        agent = create_openai_functions_agent(self.llm, self.tools, prompt)
        return AgentExecutor(
            agent=agent, 
            tools=self.tools, 
            verbose=True,
            handle_parsing_errors=True
        )
    
    def get_suggestion(self, 
                      user_input: str, 
                      current_metadata: Dict[str, Any], 
                      chat_history: List[Dict[str, str]]) -> str:
        
        context = json.dumps(current_metadata, indent=2) if current_metadata else "No fields filled yet"

        lc_history = []
        for msg in chat_history:
            if msg["role"] == "user":
                lc_history.append(HumanMessage(content=msg["content"]))
            else:
                lc_history.append(SystemMessage(content=msg["content"]))
        
        try:
            response = self.agent_executor.invoke({
                "input": user_input,
                "context": context,
                "chat_history": lc_history
            })
            return response["output"]
        except Exception as e:
            return f"Error getting suggestion: {str(e)}"
