from typing import Optional
from typing import List, Dict

from app.schemas.ner import NerQuery, NerEntities, NerEntity

from app.main import nlp_model


def get_entities(query: NerQuery) -> NerEntities:
    query_dict = query.dict(exclude_unset=True)
    doc = nlp_model(query_dict["sentence"])
    entities = [
        NerEntity(
            text=str(x), entity=x.label_, pos=i, start=x.start_char, end=x.end_char
        )
        for i, x in enumerate(doc.ents)
    ]

    ner = nlp_model._meta["name"] + "_" + nlp_model._meta["version"]
    return NerEntities(entities=entities, ner=ner)
