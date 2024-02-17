from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select


async def query_executor(query: Select, session: AsyncSession):
    """Run sync query and return sqlalchemy iterator onject."""
    query_db = await session.execute(query)
    await session.commit()
    return query_db
