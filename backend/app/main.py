from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db, engine, Base
from app import models

app = FastAPI(title="Real-Time Meeting Intelligence Engine")
# Creates any missing tables in PostgreSQL when the server starts.
Base.metadata.create_all(bind=engine)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Backend is running"}


# Depends(get_db) = "FastAPI, please give me a database session."
@app.get("/api/db-check")
def db_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))  # simplest possible database question
    return {"status": "ok", "message": "Database connected"}