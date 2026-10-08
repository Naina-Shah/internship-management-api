from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String, func, DateTime
from models.base import Base
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.internship import Internship


class Student(Base):
    __tablename__ = "student"

    s_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    s_name: Mapped[str] = mapped_column(
        String(30)
    )

    s_email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    s_password: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    s_date: Mapped[datetime.datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    e_date: Mapped[datetime.datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    interni: Mapped[list["Internship"]] = relationship(
        "Internship",
        back_populates="stu"
    )



    

    

  
