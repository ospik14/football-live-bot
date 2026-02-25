from pydantic import BaseModel

class LeagueBase(BaseModel):
    id: int
    name: str