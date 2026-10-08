from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from models.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.supervisor import Supervisor
    from models.student import Student


class Internship(Base):
    __tablename__ = "internship"

    i_id: Mapped[int] = mapped_column(primary_key=True)

    i_name: Mapped[str] = mapped_column(
        String(300)
    )

    t_id: Mapped[int] = mapped_column(
        ForeignKey("supervisor.t_id") , unique=True
    )

    s_id: Mapped[int | None] = mapped_column(
        ForeignKey("student.s_id"),
        nullable=True
    )

    sup: Mapped["Supervisor"] = relationship(
        "Supervisor",
        back_populates="intern"
    )

    stu: Mapped["Student"] = relationship(
        "Student",
        back_populates="interni"
    )