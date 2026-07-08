from sqlalchemy.orm import Session

from app.repository.url_repository import UrlRepository
from app.schemas.url_schema import UrlRequest
from app.utils.encoder import Base62Encoder
from app.utils.obfuscator import Obfuscator
from app.utils.id_generator import id_generator

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