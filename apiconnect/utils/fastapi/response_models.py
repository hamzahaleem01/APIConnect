from datetime import datetime
from typing import List

from pydantic import BaseModel


class TweetInformation(BaseModel):
    """Schema response Tweet Information."""

    user: str
    date_created: datetime
    number_of_likes: int
    source_of_tweet: str
    tweet: str


class ResponseModel(BaseModel):
    """Schema response body endpoint."""

    tweets: List[TweetInformation]
