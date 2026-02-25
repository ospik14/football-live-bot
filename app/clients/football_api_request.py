from curl_cffi.requests import AsyncSession
import asyncio
from datetime import datetime, UTC

async def get_football_data(url: str):
    async with AsyncSession() as session:
        try:
            response = await session.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "en-US,en;q=0.9,uk;q=0.8",
                    "Origin": "https://www.sofascore.com",
                    "Referer": "https://www.sofascore.com/",
                }
            )
            if not response.status_code == 200: return

            data = response.json()
            events = data.get("events", [])
            if events:
                return events
                #print(f"Приклад: {events[0]['homeTeam']['name']} {events[0]['homeScore']['current']}:{events[0]['awayScore']['current']} {events[0]['awayTeam']['name']}")
                #print(events[0])
        except Exception as e:
            print(e)
