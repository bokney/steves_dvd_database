
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .persistence.schema import init_db
from .persistence.store import load_media, load_copies, save_media, save_copy

DB_PATH = Path("steves_collection.db")
TEMPLATES_DIR = Path(__file__).parent / "templates"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db(DB_PATH)
    yield


app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory=TEMPLATES_DIR)


# ── Media ──────────────────────────────────────────────────────────────────────

@app.get("/")
def index(request: Request, title: str | None = None):
    media = load_media(DB_PATH, title=title)
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "media": media,
            "search": title or "",
        }
    )


@app.get("/media/add")
def add_media_form(request: Request):
    return templates.TemplateResponse(request, "add_media.html")


@app.post("/media/add")
def add_media(
    title: str = Form(...),
    release_year: str = Form(""),
    rating: str = Form(""),
):
    year = int(release_year) if release_year.strip() else None
    stars = int(rating) if rating.strip() else None
    save_media(DB_PATH, title=title.strip(), release_year=year, rating=stars)
    return RedirectResponse("/", status_code=303)


@app.get("/media/{id}")
def media_detail(request: Request, id: int):
    results = load_media(DB_PATH, id=id)
    if not results:
        return templates.TemplateResponse(request, "404.html", status_code=404)
    media = results[0]
    copies = load_copies(DB_PATH)
    media_copies = [c for c in copies if c.media_id == id]
    return templates.TemplateResponse(
        request, 
        "media_detail.html", 
        {
            "media": media,
            "copies": media_copies,
        }
    )


# ── Copies ─────────────────────────────────────────────────────────────────────

@app.get("/copies/add")
def add_copy_form(request: Request):
    all_media = load_media(DB_PATH)
    return templates.TemplateResponse(
        request, 
        "add_copy.html", 
        {
            "all_media": all_media,
        }
    )


@app.post("/copies/add")
def add_copy(
    media_id: int = Form(...),
    format: str = Form(...),
    notes: str = Form(""),
):
    save_copy(DB_PATH, media_id=media_id, format=format, notes=notes.strip() or None)
    return RedirectResponse(f"/media/{media_id}", status_code=303)
