from fastapi import FastAPI
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


# Sample data
organisations_db = [
    Organisation(id=1, name="Acme Corp", description="A technology company"),
    Organisation(id=2, name="Global Industries", description="Manufacturing and logistics"),
    Organisation(id=3, name="Tech Solutions", description="Software development services"),
]


@app.get("/organisations", response_model=list[Organisation])
def get_organisations():
    """Retrieve a list of all organisations."""
    return organisations_db
