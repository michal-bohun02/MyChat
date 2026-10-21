from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.ollama_service import send_prompt, get_answer

ollama_router = APIRouter(prefix="/ollama", tags=["ollama"])


class PromptRequest(BaseModel):
    prompt: str
@ollama_router.post("/get_response", tags=["ollama"], summary="Get response from Ollama")
async def get_response(prompt:PromptRequest):
    messages = [
        {'role': 'system', 'content': 'Jesteś pomocnym asystentem. Odpowiadaj zawsze po polsku.'},
        {"role": "user", "content": prompt.prompt}]
    stream = await send_prompt(messages)
    return await get_answer(stream,messages)