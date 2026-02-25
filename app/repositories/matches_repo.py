from datetime import datetime, date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.tables_models import Match

async def get_todays_matches(session: AsyncSession, date: datetime):
    query = (
        select(Match)
        .where((Match.start_time).date() == date)
    )
    matches = await session.execute(query)

    return matches.scalars().all()