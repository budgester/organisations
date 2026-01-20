import json
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(
    title="Organisations API",
    description="API for managing organisations",
    version="1.0.0",
)

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


class Organisation(BaseModel):
    id: int
    name: str
    acronym: str
    owner: str
    description: str | None = None


def load_organisations() -> list[Organisation]:
    data_file = Path(__file__).parent / "data" / "organisations.json"
    with open(data_file) as f:
        data = json.load(f)
    return [Organisation(**org) for org in data]


organisations_db = load_organisations()


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    """Display organisations as an HTML table."""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "organisations": organisations_db},
    )


@app.get("/organisations", response_model=list[Organisation])
def get_organisations():
    """Retrieve a list of all organisations."""
    return organisations_db


@app.get("/organisations/{acronym}", response_model=Organisation)
def get_organisation_by_acronym(acronym: str):
    """Retrieve an organisation by its acronym."""
    acronym_upper = acronym.upper()
    for org in organisations_db:
        if org.acronym == acronym_upper:
            return org
    raise HTTPException(status_code=404, detail=f"Organisation with acronym '{acronym_upper}' not found")
