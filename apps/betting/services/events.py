from typing import List

from apps.betting.models.events import Event


class EventsService:
    """Service of events."""

    async def get_list(self) -> List[Event]:
        """Return events list"""
