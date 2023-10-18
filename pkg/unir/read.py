from pathlib import Path
from json import loads
from datetime import datetime, timedelta

__DATA_PATH = Path("data.json").absolute()

def __read_events_from_file()->list[dict]:
    if __DATA_PATH.exists():
        with open(file=__DATA_PATH, mode="r", encoding="utf-8") as f:
            return loads(f.read())
    else:
        print("NO data to read")

def __build_summary(**kwargs):
    description = ""
    theme_name = kwargs.get("Nombre_tema")
    week = kwargs.get("Semana")
    subthemes = kwargs.get("Subtemas")
    activities = kwargs.get("Actividades")
    if theme_name and kwargs.get("Tema")!= "":
        description += f"{theme_name}\n"
    if week:
        description += f"{week}\n"
    if subthemes:
        description +="Subtemas:\n"
        for subtheme in subthemes:
            description += f"{subtheme}\n"
    if activities:
        description += f"Actividades: {activities}"
    return description

def __format_events(events:list[dict]):
    formatted_events = []
    for event in events:
        summary = event.get("Tema") if event.get("Tema") != "" else event.get("Nombre_tema")
        init_date = datetime.strptime(event.get("Fecha_inicio"), "%d/%m/%Y").date().strftime("%Y-%m-%d")
        end_date = datetime.strptime(event.get("Fecha_fin"), "%d/%m/%Y").date()
        end_date = end_date + timedelta(days=1)
        end_date = end_date.strftime("%Y-%m-%d")
        formatted_events.append({
            "summary":  summary,
            "init_date": init_date,
            "end_date": end_date,
            "description": __build_summary(**event)
        })
    return formatted_events

def read_events():
    unformatted_events = __read_events_from_file()
    return  __format_events(unformatted_events)
