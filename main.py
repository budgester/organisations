import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="Organisations API",
    description="API for managing organisations",
    version="1.0.0",
)


class Organisation(BaseModel):
    id: int
    name: str
    description: str | None = None


def load_organisations() -> list[Organisation]:
    data_file = Path(__file__).parent / "data" / "organisations.json"
    with open(data_file) as f:
        data = json.load(f)
    return [Organisation(**org) for org in data]


organisations_db = load_organisations()


@app.get("/", response_class=HTMLResponse)
def root():
    """Display organisations as an HTML table."""
    rows = "".join(
        f"<tr><td>{org.id}</td><td>{org.name}</td><td>{org.description or ''}</td></tr>"
        for org in organisations_db
    )
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Organisations</title>
        <style>
            body {{ font-family: sans-serif; margin: 40px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            tr:hover {{ background-color: #ddd; }}
        </style>
    </head>
    <body>
        <h1>Organisations</h1>
        <table>
            <tr><th>ID</th><th>Name</th><th>Description</th></tr>
            {rows}
        </table>
        <p><a href="/docs">API Documentation</a></p>
    </body>
    </html>
    """


@app.get("/organisations", response_model=list[Organisation])
def get_organisations():
    """Retrieve a list of all organisations."""
    return organisations_db
