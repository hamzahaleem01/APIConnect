from pydantic import BaseModel, ConfigDict
from typing import Optional


class ModelIncoming(BaseModel):
    """Schema request body endpoint."""

    twitter_user: Optional[str] = None
    source_of_tweet: Optional[str] = None
    tweet_filter: Optional[str] = None
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "twitter_user": "TwitterDev",
                "source_of_tweet": "Twitter for Android",
                "tweet_filter": "technology",
            },
        }
    )
