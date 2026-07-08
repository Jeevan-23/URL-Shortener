from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import BigInteger

from app.database import Base


class Url(Base):
    __tablename__ = "urls"


    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    short_code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=True
    )

    original_url: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    click_count: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )