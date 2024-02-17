from apiconnect.utils.database.connector import DBconnector
from typing import Optional
from sqlalchemy import select
from apiconnect.utils.database.orms import Tweets
from apiconnect.utils.database.utils import query_executor


async def wrapper_general_twitter(
    user: Optional[str],
    source: Optional[str],
    filter: Optional[str],
    connector: DBconnector,
):
    async with connector.async_session_factory() as session:
        if not source and not filter:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where(Tweets.twitter_user == user)
        elif not user and not filter:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where(Tweets.source_of_tweet == source)
        elif not source and not user:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where(Tweets.tweet.like(f"%{filter}%"))
        elif not user:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where(
                (Tweets.source_of_tweet == source) & (Tweets.tweet.like(f"%{filter}%"))
            )
        elif not source:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where((Tweets.twitter_user == user) & (Tweets.tweet.like(f"%{filter}%")))
        elif not filter:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where((Tweets.source_of_tweet == source) & (Tweets.twitter_user == user))
        else:
            query = select(
                Tweets.twitter_user,
                Tweets.date_created,
                Tweets.number_of_likes,
                Tweets.source_of_tweet,
                Tweets.tweet,
            ).where(
                (Tweets.source_of_tweet == source)
                & (Tweets.twitter_user == user)
                & (Tweets.tweet.like(f"%{filter}%"))
            )

        query_result = await query_executor(query=query, session=session)
        col_alias = (
            "user",
            "date_created",
            "number_of_likes",
            "source_of_tweet",
            "tweet",
        )
        tweet_info = [dict(zip(col_alias, row)) for row in query_result]
        print(tweet_info)
        return {"tweets": tweet_info}
