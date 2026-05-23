from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import SMessageAdd
from repository import MessageRepository


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)

@router.post("")
async def add_message(
    message: Annotated[SMessageAdd, Depends()],
):
    message_id = await MessageRepository.add_message(message)
    return {"ok": True, "message_id": message_id}


@router.get("")
async def get_messages():
    messages = await MessageRepository.get_all()
    return {"messages": messages}
