from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repository.url_repository import UrlRepository
from app.schemas.url_schema import UrlRequest
from app.utils.encoder import Base62Encoder
from app.utils.id_generator import id_generator
from app.utils.obfuscator import Obfuscator


class UrlService:

    def __init__(self):
        self.repository = UrlRepository()

    def shorten_url(
        self,
        db: Session,
        request: UrlRequest
    ):

        generated_id = id_generator.next_id()

        obfuscated_id = Obfuscator.obfuscate(generated_id)

        short_code = Base62Encoder.encode(obfuscated_id)

        url = self.repository.create(
            db=db,
            id=generated_id,
            short_code=short_code,
            original_url=str(request.url)
        )

        return {
            "id": url.id,
            "short_code": url.short_code,
            "short_url": f"http://localhost:8000/{url.short_code}",
            "original_url": url.original_url
        }

    def redirect(
        self,
        db: Session,
        short_code: str
    ) -> str:

        decoded = Base62Encoder.decode(short_code)

        original_id = Obfuscator.deobfuscate(decoded)

        url = self.repository.find_by_id(
            db=db,
            id=original_id
        )

        if url is None:
            raise HTTPException(
                status_code=404,
                detail="Short URL not found"
            )

        url.click_count += 1

        db.commit()

        return url.original_url