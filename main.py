from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

@app.get("/status")
async def root():
    return {"status": "Rockin", "message": "Hamlin 4 Champ"}