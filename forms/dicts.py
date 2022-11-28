from pydantic import BaseModel


class BaseDictForm(BaseModel):
    slug: str
    name: str

    class Config:
        orm_mode = True
