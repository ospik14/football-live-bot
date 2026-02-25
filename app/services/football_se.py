from datetime import datetime, UTC
from repositories.matches_repo import get_todays_matches
from core.database import async_session_local
from clients.football_api_request import get_football_data
from schemas.match import MatchBase
from schemas.league import LeagueBase
from schemas.team import TeamBase

TOP_LEAGUES = {
    # === ТОП-5 Європи ===
    17: "Premier League",      # Англія
    8:  "LaLiga",              # Іспанія
    23: "Serie A",             # Італія
    35: "Bundesliga",          # Німеччина
    34: "Ligue 1",             # Франція

    # === Єврокубки ===
    7:  "UEFA Champions League", 
    679: "UEFA Europa League",
    17015: "UEFA Europa Conference League",

    # === Україна ===
    69: "Ukrainian Premier League", # УПЛ
    2113: "Ukrainian Cup",          # Кубок України

    # === Міжнародні (Збірні) ===
    16: "World Cup",               # Чемпіонат Світу
    1:  "European Championship",   # Євро
    1755: "UEFA Nations League",   # Ліга Націй

    # === Топові національні кубки (опціонально) ===
    19: "FA Cup",              # Англія
    138: "Copa del Rey",       # Іспанія
    137: "Coppa Italia",       # Італія
    134: "DFB Pokal",          # Німеччина
}

async def match_processor(events: list[dict]):
    white_list_ids = set(TOP_LEAGUES.keys())
    matches = []
    leagues = {}
    teams = {}

    for event in events:
        league_id = event.get('tournament', {}).get('uniqueTournament', {}).get('id')
        home_team_id=event.get('homeTeam', {}).get('id')
        away_team_id=event.get('awayTeam', {}).get('id')
        if league_id in white_list_ids:
            match = MatchBase(
                id=event.get('id'),
                home_team_id=home_team_id,
                away_team_id=away_team_id,
                home_score=event.get('homeScore', {}).get('current'),
                away_score=event.get('awayScore', {}).get('current'),
                league_id=league_id,
                status='not_started',
                start_time=event.get('startTimestamp')
            )
            league = LeagueBase(
                id=league_id,
                name=event.get('tournament', {}).get('name')
            )
            home_team = TeamBase(
                id=home_team_id,
                name=event.get('homeTeam', {}).get('name')
            )
            away_team = TeamBase(
                id=away_team_id,
                name=event.get('awayTeam', {}).get('name')
            )

            matches.append(match)
            teams[home_team_id] = home_team
            teams[away_team_id] = away_team
            leagues[league_id] = league
    
    return {
        'teams': list(teams.values()),
        'leagues': list(leagues.values()),
        'matches': matches
    }


async def find_todays_matches():
    current_date = datetime.now(tz=UTC).date()

    async with async_session_local() as session:
        matches = await get_todays_matches(session, current_date)
        if matches: return matches

        url = f'https://api.sofascore.com/api/v1/sport/football/scheduled-events/{current_date}'
        events = await get_football_data(url)