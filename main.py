import datetime
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel


from sqlalchemy.orm import Session

from db.database import get_db,engine

from models.base import Base
from models.student import Student
from models.internship import Internship
from models.supervisor import Supervisor
from models.st_in import StudentInternship
print(Base.metadata.tables.keys())
(Base.metadata.create_all(bind=engine))

app=FastAPI()

def Password(password):
   
    try:
        if len(password) < 8 :
            return ('Password must contain uppercase, lowercase, digit and special characters')
        elif len(password) >= 8:
            if not any(char.isupper() for char in password):
                raise ValueError("Password Must Contain a Captial Letter ")
            if not any(char.islower() for char in password):
                raise ValueError("Password must Contain a small Letter")

            if not any(char.isdigit() for char in password):
                raise  ValueError("password Must Contain a digit")
            if not any(not char.isalnum() for char in password):
                raise ValueError("Password Must have a special character like !,$,@ ")

        return password

        
    except:
        raise ValueError("Wrond Password .") 
        
        
    


class Students(BaseModel):
  
    s_name: str
    s_email: str
    s_password: str
    

# ============================Create Post ====================

@app.post("/students")

def create_students(students:Students, db_Session = Depends(get_db)):

    '''join_date = datetime.datetime.now().replace(second=0, microsecond=0)
    end_date = join_date + datetime.timedelta(days=30)'''


    Password(students.s_password)
    new_students= Student(
        s_name= students.s_name,
        s_email = students.s_email,
        s_password= students.s_password
    
        
    )

    db_Session.add(new_students)
    db_Session.commit()
    db_Session.refresh(new_students)

    return new_students


# ============================= Get Post =========
@app.get("/students")
def view_students(db_Session= Depends(get_db) ):
    candidates= db_Session.query(Student).all()
    return candidates



#========================================================= Internships =====================================================
@app.post("/students/{student_id}/internships/{internship_id}")
def register_internship(
    student_id: int,
    internship_id: int,
    db_Session=Depends(get_db)
):

    # 1. Check student
    student = db_Session.query(Student).filter(
        Student.s_id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # 2. Check active internship
    now = datetime.datetime.now().replace(
        second=0,
        microsecond=0
    )

    if student.e_date is not None and student.e_date > now:
        raise HTTPException(
            status_code=400,
            detail="Student already has an active internship"
        )

    # 3. Check internship
    internship = db_Session.query(Internship).filter(
        Internship.i_id == internship_id
    ).first()

    if not internship:
        raise HTTPException(
            status_code=404,
            detail="Internship not found"
        )

    # 4. Check if student already took this internship
    previous = db_Session.query(StudentInternship).filter(
        StudentInternship.student_id == student_id,
        StudentInternship.internship_id == internship_id
    ).first()

    if previous:
        raise HTTPException(
            status_code=400,
            detail="Student has already completed or taken this internship"
        )

    # 5. Set internship dates
    internship.s_id = student_id
    student.s_date = now
    student.e_date = student.s_date + datetime.timedelta(days=30)

    # 6. Save internship history
    new_record = StudentInternship(
        student_id=student_id,
        internship_id=internship_id,
        start_date=student.s_date,
        end_date=student.e_date
    )

    db_Session.add(new_record)
    db_Session.commit()

    # 7. Response
    return {
        "student": student.s_name,
        "internship": internship.i_name,
        "start_date": student.s_date,
        "end_date": student.e_date,
        "mentor": internship.sup.t_name
    }

  

#=======================================================Supervisor ========================================================
class Supervisors(BaseModel):
    t_name: str
    t_email: str

@app.post("/supervisors")
def create_supervisor(supervisors:Supervisors, db_Session = Depends(get_db)):
    new_supervisor= Supervisor(
        
        t_name= supervisors.t_name,
        t_email= supervisors.t_email
    )
    db_Session.add(new_supervisor)
    db_Session.commit()
    db_Session.refresh(new_supervisor)
    return new_supervisor



@app.get("/supervisors")
def get_supervisors(db_Session = Depends(get_db)):
    teacher=db_Session.query(Supervisor).all()
    return teacher