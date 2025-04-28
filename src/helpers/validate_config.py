
from typing import Any, Dict, Union

from haystack.components.generators.chat import OpenAIChatGenerator
from haystack_integrations.document_stores.opensearch import OpenSearchDocumentStore
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
from haystack.document_stores.in_memory import InMemoryDocumentStore
from pydantic import BaseModel
import hydra


class HydraConfig(BaseModel):
    generator: OpenAIChatGenerator
    db: Union[OpenSearchDocumentStore, QdrantDocumentStore, InMemoryDocumentStore]
    prompts: Dict[str, Any]
    query: str

    class Config:
        arbitrary_types_allowed = True
    def __init__(self, **data):
        # this instantiate will generate the instances for the dictionary 
        # that includes the item _target_
        data = hydra.utils.instantiate(data)
        super().__init__(**data)
