from fastapi import Depends, FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware,
)  #  Cross Origin Resource Sharing (CORS) management

from tortoise import Tortoise  # enable schemas to read relationship between models

from app.database.config import TORTOISE_ORM  # application models config
from app.database.register import register_tortoise

from app.database.models import UserDB
from app.services.users import current_active_user
from app.services.pytorch import load_lang, load_pytorch_checkpoint_inference

from pathlib import Path

import spacy
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#########################################################################
# MODELS LOADERS
#########################################################################
# paths
workspace = "datas"
name = "imprimeur"
target = "models"
source = "source"

## SPACY
nlp_name = "imprimerie_NER_CATEG"
nlp_model = spacy.load(Path(workspace).joinpath(name, target, nlp_name))
print(f"MAIN nlp_model {nlp_model._meta}")

## PYTORCH
input_lang_name = "imprimerie_brute"
output_lang_name = "imprimerie_normalisee"

PATH_SEQ2SEQ = Path(workspace).joinpath(name, target)
PATH_SEQ2SEQ_MODEL = PATH_SEQ2SEQ.joinpath(
    "seq2seq_imprimerie_brute_imprimerie_normalisee_512_0.01_1641223250_1.38325.dill"
)
seq2seq_input_lang, seq2seq_output_lang = load_lang(
    input_lang_name, output_lang_name, Path(PATH_SEQ2SEQ)
)
seq2seq_encoder, seq2seq_decoder = load_pytorch_checkpoint_inference(
    Path(PATH_SEQ2SEQ_MODEL), seq2seq_input_lang, seq2seq_output_lang, device, 512
)


## TORTOISE
# enable schemas to read relationship between models
Tortoise.init_models(["app.database.models"], "models")

from app.routes import users, products, translation, ner

#########################################################################
# APP
#########################################################################
app = FastAPI()

#  Cross Origin Resource Sharing (CORS) management
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, tags=["users"])
app.include_router(products.router, tags=["products"])
app.include_router(ner.router, tags=["named entities recognitions"])
app.include_router(translation.router, tags=["translations"])


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)


@app.get("/")
async def home():
    return {
        "msg": f"wercome on our character level sequence 2 sequence machine translation demo"
    }


@app.get("/status")
async def health():
    return {"msg": "status up"}
