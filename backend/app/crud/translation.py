from pathlib import Path

from app.schemas.translation import (
    TranslationInSchema,
    TranslationOutSchema,
    EntitySchema,
)

from app.services.pytorch import evaluate

# loading dir names
from app.main import (
    seq2seq_input_lang,
    seq2seq_output_lang,
    seq2seq_encoder,
    seq2seq_decoder,
)

"""
je suis dans crud translate_entities, entities: 
entities=[EntitySchema(text='500', entity='EXEMPLAIRES', pos=0, start=14, end=17), EntitySchema(text='flyers', entity='PRODUCT', pos=1, start=18, end=24), EntitySchema(text='quadri r/v', entity='IMPRESSION', pos=2, start=28, end=38), EntitySchema(text='format a4', entity='FORMAT', pos=3, start=40, end=49)] model='imprimeur'

translate_entity, entity: ('entities', [EntitySchema(text='500', entity='EXEMPLAIRES', pos=0, start=14, end=17), EntitySchema(text='flyers', entity='PRODUCT', pos=1, start=18, end=24), EntitySchema(text='quadri r/v', entity='IMPRESSION', pos=2, start=28, end=38), EntitySchema(text='format a4', entity='FORMAT', pos=3, start=40, end=49)])
"""


def translate_entity(entity: EntitySchema, input_lang, output_lang, encoder, decoder):

    if entity["entity"] in ["FORMAT", "GRAMMAGES", "PAPIER", "IMPRESSION", "PRODUCT"]:
        text = entity["entity"][:2] + "|" + entity["text"]
        output_chars, attentions = evaluate(
            encoder, decoder, input_lang, output_lang, text
        )
        entity["text"] = "".join(output_chars).rstrip("<EOS>")

    return EntitySchema(**entity)


async def translate_entities(entities: TranslationInSchema) -> TranslationOutSchema:

    ents = [ent.dict(exclude_unset=True) for ent in entities.entities]

    translation = []

    entities = list(
        map(
            lambda x: translate_entity(
                x,
                seq2seq_input_lang,
                seq2seq_output_lang,
                seq2seq_encoder,
                seq2seq_decoder,
            ),
            ents,
        )
    )

    return {"entities": entities}
