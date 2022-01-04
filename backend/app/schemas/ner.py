from pydantic import BaseModel
from typing import Optional
from typing import List, Dict, Tuple


class NerQuery(BaseModel):
    sentence: str = "urgent, devis pour 6000 flyers a5, quadri rv, cdm, sous film par paquet de 100, livraison 72, merci"


class NerEntity(BaseModel):
    text: str
    entity: str
    pos: int
    start: int
    end: int


class NerEntities(BaseModel):
    entities: List[NerEntity]
    ner: str
