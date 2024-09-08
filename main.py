import uvicorn
from fastapi import FastAPI


from logging_settings import LoggerSetup

import logging

# Setting up the root logger

logger_setup = LoggerSetup()

LOGGER = logging.getLogger(__name__)


def init_app():
    apps = FastAPI(
        title="Simple To Do App", description="To do organizer app", version="1.0.0"
    )

    @apps.on_event("startup")
    async def startup():
        LOGGER.info("To Do App is starting up....")
        pass

    @apps.on_event("shutdown")
    async def shutdown():
        LOGGER.info("To Do App is Shutting Down....")

        pass

    @apps.get("/")
    def home():
        return "Welcome to To Do App Home"

    from routers.home import router

    apps.include_router(router=router)

    return apps


app = init_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8800, reload=True)
