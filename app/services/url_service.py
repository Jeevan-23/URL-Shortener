from sqlalchemy.orm import Session

from app.repository.url_repository import UrlRepository
from app.schemas.url_schema import UrlRequest


class UrlService:

    def __init__(self):
        self.repository = UrlRepository()

    def shorten_url(
        self,
        db: Session,
        request: UrlRequest
    ):

        return self.repository.save(
            db,
            request.url,
            "TEMP"
        )