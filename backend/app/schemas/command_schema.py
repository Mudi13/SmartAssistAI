from pydantic import BaseModel


class CommandRequest(BaseModel):
    text: str


class CommandResponse(BaseModel):
    response: str
    log_id: int