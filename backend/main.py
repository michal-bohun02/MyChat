from fastapi import FastAPI
from backend.routes import ollama_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ollama_routes.ollama_router)

@app.get("/")
def root():
    return {"message": "Hello World"}
