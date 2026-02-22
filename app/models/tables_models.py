import enum
from datetime import datetime
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime, String, func, BigInteger, Integer

class Status(enum.Enum):
    NOT_STARTED = 'not_started'
    LIVE = 'live'
    FINISHED = 'finished'

class User(Base):
    __tablename__='users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

class UserSub(Base):
    __tablename__ = 'user_subs'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'))
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))

class League(Base):
    __tablename__='leagues'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String)
    
class Team(Base):
    __tablename__='teams'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String)
    country: Mapped[str] = mapped_column(String)

class Match(Base):
    __tablename__='matches'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    home_team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    away_team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    home_score: Mapped[int] = mapped_column(Integer, default=0)
    away_score: Mapped[int] = mapped_column(Integer, default=0)
    league_id: Mapped[int] = mapped_column(ForeignKey('leagues.id'))
    status: Mapped[Status] 
    start_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))