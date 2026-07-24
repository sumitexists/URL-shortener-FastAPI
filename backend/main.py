from typing import Annotated
from fastapi import Body, FastAPI, Depends, HTTPException, Path
from fastapi.responses import RedirectResponse
from pydantic import HttpUrl
from contextlib import asynccontextmanager
from backend.db import init_db, get_session
from backend.models import UrlBase
from sqlmodel import Session, select
from backend.utils import url_saver

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/url", status_code=201, summary="Creates the shortened URL", 
    description="You just have to post the URL within a key-value pair with url_data.")
async def create_shortend_url (
    url_data: Annotated[
        HttpUrl, 
        Body(embed=True,
              examples=["https://www.example.com"],)
             
    ],
    session : Session = Depends(get_session)
)-> dict:
    try:
        url = url_saver(url_data = url_data, session = session)
    except:
        session.rollback()
        statement = select(UrlBase).where(UrlBase.url == str(url_data))
        url = session.exec(statement).first()

    return {"shortend_url" : f"http://localhost:8000/{url.shortend_url}"}

@app.get("/{shortend_url}", status_code=307, response_model = dict)
async def redirect_url(shortend_url:Annotated[str , Path(title="Redirects to URL",
            description="Redirects using the shortened URL to the real URL for which it was created.",
            example="ab12Ew")],session : Session = Depends(get_session)):
        """
        This endpoint redirects to an external site.
        No response schema will be shown in Swagger UI.
        """
        statement = select(UrlBase).where(UrlBase.shortend_url == shortend_url)
        url_entry = session.exec(statement).first()
        
        if not url_entry:
            raise HTTPException(status_code=404, detail="URL not found")
            
        return RedirectResponse(url=url_entry.url)
