from typing import Any, Dict

from graph.state import GraphState
from ingestor.ingestion import retriever

def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIVE---")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}