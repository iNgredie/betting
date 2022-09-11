from pydantic import BaseModel


class BaseEvent(BaseModel):
    """Base event schema."""


class Event(BaseEvent):
    """Event schema."""
