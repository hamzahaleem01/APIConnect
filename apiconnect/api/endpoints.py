from fastapi import APIRouter, Request, Depends
from typing import Annotated
from apiconnect.utils.fastapi.models_incoming import ModelIncoming
from apiconnect.utils.fastapi.response_models import ResponseModel
import apiconnect.backend.general as general


router = APIRouter(responses={400: {"detail": "Validation Error"}})


@router.post("/tweets", response_model=ResponseModel)
async def get_recommendations(request: Request, body: ModelIncoming):
    """Get feed based on given parameters."""
    return await general.wrapper_general_twitter(
        user=body.twitter_user,
        source=body.source_of_tweet,
        filter=body.tweet_filter,
        connector=request.app.state.db_connector,
    )
