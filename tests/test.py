import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError, DBAPIError

from db.database import engine


def test_seventh_internship_rejected():
    with engine.connect() as conn:
        with pytest.raises(DBAPIError):
            conn.execute(
                text("""
                    INSERT INTO internship (i_name, t_id)
                    VALUES ('Test Internship', 1)
                """)
            )


def test_seventh_supervisor_rejected():
    with engine.connect() as conn:
        with pytest.raises(DBAPIError):
            conn.execute(
                text("""
                    INSERT INTO supervisor (t_name, t_email)
                    VALUES ('Test Supervisor', 'test@example.com')
                """)
            )


def test_duplicate_supervisor_rejected():
    with engine.connect() as conn:
        with pytest.raises(IntegrityError):
            conn.execute(
                text("""
                    UPDATE internship
                    SET t_id = 1
                    WHERE i_id = 2
                """)
            )


def test_duplicate_student_email_rejected():
    with engine.connect() as conn:
        email = conn.execute(
            text("SELECT s_email FROM student LIMIT 1")
        ).scalar()

        if email is None:
            pytest.skip("No student exists")

        with pytest.raises(IntegrityError):
            conn.execute(
                text("""
                    INSERT INTO student
                    (s_name, s_email, s_password)
                    VALUES
                    ('Test Student', :email, 'password123')
                """),
                {"email": email}
            )


def test_duplicate_student_internship_rejected():
    with engine.connect() as conn:
        record = conn.execute(
            text("""
                SELECT student_id, internship_id
                FROM student_internship
                LIMIT 1
            """)
        ).first()

        if record is None:
            pytest.skip("No internship record exists")

        with pytest.raises(IntegrityError):
            conn.execute(
                text("""
                    INSERT INTO student_internship
                    (student_id, internship_id, start_date, end_date)
                    VALUES
                    (:student_id, :internship_id,
                     '2026-01-01 10:00:00',
                     '2026-01-31 10:00:00')
                """),
                {
                    "student_id": record.student_id,
                    "internship_id": record.internship_id
                }
            )