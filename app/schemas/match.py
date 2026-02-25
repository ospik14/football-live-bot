from pydantic import BaseModel
from datetime import datetime
from models.tables_models import Status

class MatchBase(BaseModel):
    id: int
    home_team_id: int
    away_team_id: int
    home_score: int = 0
    away_score: int = 0
    league_id: int
    status: Status
    start_time: datetime