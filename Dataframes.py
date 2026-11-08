import pandas as pd
from bs4 import BeautifulSoup
import requests
import re, time

#all data 1986 and later has full data
historical_data = pd.read_csv ("C:/Users/Joshu/Documents/2500project/Historical_data.csv", usecols=[
    'schedule_date',
    'schedule_season',
    'schedule_week',
    'schedule_playoff',
    'team_home',
    'score_home',
    'score_away',
    'team_away',
    'team_favorite_id',
    'spread_favorite',
    'over_under_line',
    'stadium',
    'stadium_neutral',
    'weather_temperature',
    'weather_wind_mph',
    'weather_humidity',
    'weather_detail'
    ] )



def get_week(week, pick_type="against-the-spread"):
    url = f'https://www.cbssports.com/nfl/picks/experts/{pick_type}/{week}/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all("tr")
    records = []

    expert_cells = rows[0].find_all(["th", "td"])[1:]
    experts = [
        " ".join(
            x.select_one(f".AuthorHeadshotAndName-{part}").get_text(strip=True)
            for part in ("firstName", "lastName")
        )
        for x in expert_cells
    ]

    for row in rows[1:]:
        cells = row.find_all(["th", "td"])
        link = cells[0].find("a") if cells else None
        if link is None:
            continue

        m = re.search(r"NFL_(\d{8})_(\w+)@(\w+)", link.get("href", ""))
        if not m:
            continue
        
        date, away, home = m.groups()

        # cells[0] is the game; the remaining cells are one per expert
        for expert, cell in zip(experts, cells[1:]):
            text = cell.get_text(" ", strip=True)

            result = re.search(r"\b(WIN|LOSS|PUSH)\b", text)

            leftover = text.replace("WIN", "").replace("LOSS", "").replace("PUSH", "")
            pick = re.search(r"([A-Z]{2,3})\s*([+-]\d+(?:\.\d+)?)?", leftover)

            records.append({
                "week": week,
                "date": pd.to_datetime(date, format="%Y%m%d"),
                "away": away,
                "home": home,
                "expert": expert,
                "result": result.group(1) if result else None,
                "pick": pick.group(1) if pick else None,
                "line": float(pick.group(2)) if pick and pick.group(2) else None
            })
    return pd.DataFrame(records)

def get_multiple_weeks(max_week, pick_type="against-the-spread"):
    frames = []
    for week in range(1, max_week + 1):
        frames.append(get_week(week, pick_type))
        time.sleep(2)
    return pd.concat(frames, ignore_index=True)


   
print(historical_data)
print(get_multiple_weeks(4))

