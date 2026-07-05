from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.url_schema import UrlRequest
from app.services.url_service import UrlService

router = APIRouter()

service = UrlService()


@router.post("/shorten")
def shorten(
    request: UrlRequest,
    db: Session = Depends(get_db)
):
    return service.shorten_url(
        db,
        request
    )