import random
import string
from sqlmodel import select, Session
from backend.models import UrlBase
from pydantic import HttpUrl


def generate_short_slug(length=6):
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for _ in range(length))

def url_saver(url_data:HttpUrl, session: Session):
    url_data = str(url_data)
    while True:
        shortend_url = generate_short_slug()
        statement = select(UrlBase).where(UrlBase.shortend_url==shortend_url)
        existing_url = session.exec(statement).first()
        if existing_url:
            continue
        db_obj = UrlBase(url=url_data,shortend_url=shortend_url)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj