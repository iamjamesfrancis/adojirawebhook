
from typing import Union
from fastapi import FastAPI,logger
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str


@app.post("/work-item")
async def work_item(item:Union[dict, None]):
    logger.logger.info(item)
    return item
