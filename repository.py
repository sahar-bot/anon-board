from database import new_session, MessagesOrm
from main import SMessageAdd
from sqlalchemy import select
from schemas import SMessageAdd


class MessageRepository:
    @classmethod
    async def add_message(cls, data: SMessageAdd) -> int:
        async with new_session() as session:
            message_dict = data.model_dump()

            message = MessagesOrm(**message_dict)
            session.add(message)
            await session.flush()
            await session.commit()
            return message.id

    
    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(MessagesOrm)
            result = await session.execute(query)
            message_models = result.scalars().all()
            return message_models