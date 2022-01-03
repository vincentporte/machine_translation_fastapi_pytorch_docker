from fastapi import Depends, FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware,
)  #  Cross Origin Resource Sharing (CORS) management

from tortoise import Tortoise  # enable schemas to read relationship between models

from app.database.config import TORTOISE_ORM  # application models config
from app.database.register import register_tortoise

from app.database.models import UserDB
from app.core.users import current_active_user

# from src.core.predictions import Prediction


# import numpy as np
# from pathlib import Path

#########################################################################
# MODELS LOADERS
#########################################################################
## SUGGESTIONS and PRICES
# workspace = "./datas"
# name = "imprimeur"
# target = "models"
# source = "source"
# preds = Prediction(name, workspace, target, source, debug=False)
# print(f"MAIN preds {preds.name}")

## TORTOISE
# enable schemas to read relationship between models
Tortoise.init_models(["app.database.models"], "models")

from app.routes import users, products  # destinations, prices, tasks, users

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
# app.include_router(destinations.router, tags=["destinations"])
# app.include_router(prices.router, tags=["prices"])
# app.include_router(tasks.router, tags=["tasks"])

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)


@app.get("/")
async def home():
    return {
        "msg": f"wercome on our character level sequence 2 sequence machine translation demo"
    }


@app.get("/status")
async def health():
    return {"status": "up"}
