from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.command_schema import CommandRequest
from app.db.database import get_db
from app.db.models import CommandLog

from app.intents.detector import detect_intent
from app.intents.handler import handle_intent

router = APIRouter()


@router.post("/")
def process_command(request: CommandRequest,
    db: Session = Depends(get_db)):

    intent = detect_intent(request.text)

    response = handle_intent(intent)

    log = CommandLog(
        user_input=request.text,
        response=response
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return {
        "response": response,
        "log_id": log.id
    }