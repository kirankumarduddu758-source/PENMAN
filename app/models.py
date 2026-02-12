from pydantic import BaseModel

class Registration(BaseModel):
    name: str
    phone: str
    course: str

class Contact(BaseModel):
    name: str
    message: str

class Course(BaseModel):
    name: str
    duration: str
