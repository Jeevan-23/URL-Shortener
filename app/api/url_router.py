from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
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
        db=db,
        request=request
    )


@router.get("/{short_code}")
def redirect(
    short_code: str,
    db: Session = Depends(get_db)
):
    original_url = service.redirect(
        db=db,
        short_code=short_code
    )

    return RedirectResponse(
        url=original_url,
        status_code=302
    )