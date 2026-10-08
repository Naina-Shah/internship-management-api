from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, DateTime,UniqueConstraint 
import datetime

from models.base import Base


class StudentInternship(Base):
    __tablename__ = "student_internship"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    student_id: Mapped[int] = mapped_column(
        ForeignKey("student.s_id"),
        nullable=False
    )

    internship_id: Mapped[int] = mapped_column(
        ForeignKey("internship.i_id"),
        nullable=False
    )

    start_date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    end_date: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "internship_id",
            name="unique_student_internship"
        ),
    )