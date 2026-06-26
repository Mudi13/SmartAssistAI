from fastapi import FastAPI
from app.api.command import router as command_router
from app.api.chat import router as chat_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartAssist AI",
)

app.include_router(command_router, prefix="/api/chat", tags=["Commands"])
app.include_router(chat_router, prefix="/api/command", tags=["Chat"])


@app.get("/")
def home(): 
    return {"message": "Welcome to SmartAssist AI 🚀"}