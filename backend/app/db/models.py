from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from app.db.database import Base


class CommandLog(Base):
    __tablename__ = "command_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String, nullable=False)
    response = Column(String, nullable=False)
    timestamp = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )