from pydantic import BaseModel

class TeamBase(BaseModel):
    id: int
    name: str
    country: str