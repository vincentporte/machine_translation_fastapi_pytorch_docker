from fastapi import APIRouter, Depends, HTTPException
from app.schemas.ner import NerQuery, NerEntities
from app.crud.ner import get_entities
from app.services.users import current_active_user

router = APIRouter()


@router.post(
    "/ner",
    response_model=NerEntities,
    dependencies=[Depends(current_active_user)],
)
async def api_ner(query: NerQuery) -> NerEntities:
    return get_entities(query)
