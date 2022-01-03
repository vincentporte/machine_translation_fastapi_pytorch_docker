from typing import Optional
from typing import List, Dict

from pydantic import BaseModel

#########################################################################
# Translation
#########################################################################


class EntitySchema(BaseModel):
    text: str
    entity: str
    pos: int
    start: int
    end: int


class TranslationInSchema(BaseModel):
    entities: List[EntitySchema]
    model: str = "imprimeur"


class TranslationOutSchema(BaseModel):
    entities: List[EntitySchema]
