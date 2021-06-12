import uvicorn
from api.models.database import database
from api.routers import common
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(common.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
