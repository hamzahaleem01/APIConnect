from apiconnect.utils.database.connector import DBconnector
from typing import Optional


async def wrapper_general_twitter(
    user: Optional[str],
    source: Optional[str],
    filter: Optional[str],
    connector: DBconnector,
):
    return user
