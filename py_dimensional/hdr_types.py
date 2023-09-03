import pydantic
import datetime
from typing import List


class PageResponse(pydantic.BaseModel):
    url: str
    page_content: str = pydantic.Field(..., alias="pageContent")
    date: datetime.datetime


class PageSearchResult(pydantic.BaseModel):
    url: str
    similarity: float
    content: str
