from pydantic import BaseModel
from typing import Optional
from typing import List, Dict, Tuple

class NerQuery(BaseModel):
    sentence: str

class NerEntity(BaseModel):
    text: str
    entity: str
    pos: int
    start: int
    end: int

class NerEntities(BaseModel):
    entities: List[NerEntity]
    ner: str