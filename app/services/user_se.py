from core.database import async_session_local
from sqlalchemy.exc import IntegrityError
from repositories.user_repo import create_user
from models.tables_models import User

async def add_new_user(user_id: int, username: str):
    async with async_session_local() as session:
        user = User(id=user_id, username=username)
        try:
            await create_user(session, user)
            await session.commit()
        except IntegrityError:
            return