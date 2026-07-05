from sqlalchemy.orm import Session

from app.models.url import Url


class UrlRepository:

    def save(
        self,
        db: Session,
        original_url: str,
        short_code: str
    ):

        url = Url(
            original_url=original_url,
            short_code=short_code
        )

        db.add(url)
        db.commit()
        db.refresh(url)

        return url