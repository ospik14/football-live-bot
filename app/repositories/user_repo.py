from sqlalchemy.ext.asyncio import AsyncSession
from models.tables_models import User

async def create_user(session: AsyncSession, user: User):
    session.add(user)