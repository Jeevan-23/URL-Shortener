from sqlalchemy.orm import Session

from app.models.url import Url


class UrlRepository:

    def create(
        self,
        db: Session,
        id: int,
        short_code: str,
        original_url: str
    ) -> Url:

        url = Url(
            id=id,
            short_code=short_code,
            original_url=original_url
        )

        db.add(url)
        db.commit()
        db.refresh(url)

        return url