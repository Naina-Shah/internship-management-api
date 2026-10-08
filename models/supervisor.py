from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import String
from models.base import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.internship import Internship


#================= Super Visor===================
class Supervisor(Base):
    __tablename__= "supervisor"
    t_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    t_name: Mapped[str] = mapped_column(
        String(500)
    )

    t_email: Mapped[str] = mapped_column(
        String(500)
    )

    intern: Mapped[list["Internship"]] = relationship(
        "Internship",
        back_populates="sup"
    )

