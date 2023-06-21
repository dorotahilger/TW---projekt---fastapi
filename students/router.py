
from fastapi import APIRouter, HTTPException
from .storage import STUDENTS, MARKS
from .schema import StudentCreateSchema, Student, Mark


router = APIRouter()
@router.get("/")
async def get_students():
    return list(STUDENTS.values())


@router.post("/")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    new_student = Student(**student.dict(), id=id)
    STUDENTS[id] = new_student
    return new_student


@router.put("/{student_id}")
async def update_item(student_id: int, first_name: str, last_name: str):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        student = STUDENTS[student_id]
        student.first_name = first_name
        student.last_name = last_name
    return student

@router.post("/{student_id}/marks/{ocena}")
async def add_mark(student_id: int, ocena: Mark):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")
    
    if student_id not in MARKS:
        MARKS[student_id] = []
    
    MARKS[student_id].append(ocena)
    return {"message": "Mark added successfully"}

@router.get("/{student_id}/marks")
async def get_marks(student_id: int):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")
    
    if student_id not in MARKS or len(MARKS[student_id]) == 0:
        return {"message": "No marks found for the student"}
    
    marks = [str(mark.name) for mark in MARKS[student_id]]
    return {", ".join(marks)}
