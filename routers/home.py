from fastapi import APIRouter
import logging

LOGGER = logging.getLogger(__name__)

router = APIRouter(prefix="/home", tags=["home"])


@router.get("")
async def welcome_home():
    LOGGER.info("Welcome to the Todo App")
    return "Welcome to the app"


@router.get("/test")
async def test():
    LOGGER.info("Welcome to the test module")
    return "Test successful"
