from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Jerzetta",
                "last_name": "Kłosińska",
            }
        }


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str

class Mark(str, Enum):
    BARDZO_DOBRY = "5.0"
    DOBRY_PLUS = "4.5"
    DOBRY = "4.0"
    DOSTATECZNY_PLUS = "3.5"
    DOSTATECZNY = "3.0"
    NIEDOSTATECZNY = "2.0"
