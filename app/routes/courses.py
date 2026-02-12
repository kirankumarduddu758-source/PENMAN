from fastapi import APIRouter

router = APIRouter(prefix="/courses", tags=["Courses"])

# Static courses for now (can move to DynamoDB later)
COURSES = [
    {"name": "Cursive Writing", "duration": "4 Weeks"},
    {"name": "Italic Writing", "duration": "4 Weeks"},
    {"name": "Calligraphy Basics", "duration": "6 Weeks"}
]

@router.get("/")
def get_courses():
    return COURSES
