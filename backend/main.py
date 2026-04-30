from fastapi import FastAPI
from backend.routes.flash import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"status": "ok"}
