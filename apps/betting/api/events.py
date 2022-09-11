from typing import List

from fastapi import APIRouter, Depends

from apps.betting.models.events import Event
from apps.betting.services.events import EventsService

router = APIRouter(
    prefix='/operations',
    tags=['operations'],
)


@router.get('/', response_model=List[Event])
async def get_events(
    service: EventsService = Depends(),
):
    return service.get_list()
