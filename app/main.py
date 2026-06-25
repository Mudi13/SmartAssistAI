from fastapi import FastAPI
from app.api.command import router as command_router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartAssist AI",
    version="1.0.0"
)

app.include_router(command_router, prefix="/api", tags=["Commands"])


@app.get("/")
def home():
    return {"message": "Welcome to SmartAssist AI 🚀"}