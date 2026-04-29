from fastapi import FastAPI
from backend.routes import router

app = FastAPI(title="Flash Boot Tool")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok"}
