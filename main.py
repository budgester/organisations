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
            th {{ background-color: #4CAF50; color: white; cursor: pointer; }}
            th:hover {{ background-color: #45a049; }}
            th::after {{ content: ' ⇅'; opacity: 0.5; }}
            th.asc::after {{ content: ' ↑'; opacity: 1; }}
            th.desc::after {{ content: ' ↓'; opacity: 1; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            tr:hover {{ background-color: #ddd; }}
            #searchBox {{ width: 100%; padding: 12px; margin-bottom: 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; }}
            #searchBox:focus {{ outline: none; border-color: #4CAF50; }}
        </style>
    </head>
    <body>
        <h1>Organisations</h1>
        <input type="text" id="searchBox" onkeyup="filterTable()" placeholder="Search organisations...">
        <table id="orgTable">
            <thead>
                <tr><th onclick="sortTable(0)">ID</th><th onclick="sortTable(1)">Name</th><th onclick="sortTable(2)">Description</th></tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
        <p>
            <a href="/docs">API Documentation</a> |
            <a href="https://github.com/budgester/organisations">GitHub</a>
        </p>
        <script>
            let sortDirection = [true, true, true];
            function sortTable(colIndex) {{
                const table = document.getElementById("orgTable");
                const tbody = table.querySelector("tbody");
                const rows = Array.from(tbody.querySelectorAll("tr"));
                const headers = table.querySelectorAll("th");

                headers.forEach((h, i) => {{
                    h.classList.remove("asc", "desc");
                    if (i === colIndex) {{
                        h.classList.add(sortDirection[colIndex] ? "asc" : "desc");
                    }}
                }});

                rows.sort((a, b) => {{
                    let aVal = a.cells[colIndex].textContent;
                    let bVal = b.cells[colIndex].textContent;
                    if (colIndex === 0) {{
                        aVal = parseInt(aVal);
                        bVal = parseInt(bVal);
                    }}
                    if (aVal < bVal) return sortDirection[colIndex] ? -1 : 1;
                    if (aVal > bVal) return sortDirection[colIndex] ? 1 : -1;
                    return 0;
                }});

                sortDirection[colIndex] = !sortDirection[colIndex];
                rows.forEach(row => tbody.appendChild(row));
            }}

            function filterTable() {{
                const query = document.getElementById("searchBox").value.toLowerCase();
                const tbody = document.getElementById("orgTable").querySelector("tbody");
                const rows = tbody.querySelectorAll("tr");

                rows.forEach(row => {{
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(query) ? "" : "none";
                }});
            }}
        </script>
    </body>
    </html>
    """


@app.get("/organisations", response_model=list[Organisation])
def get_organisations():
    """Retrieve a list of all organisations."""
    return organisations_db
