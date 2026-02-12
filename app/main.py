from fastapi import FastAPI
from mangum import Mangum

from app.routes.registration import router as registration_router
from app.routes.courses import router as courses_router
from app.routes.contact import router as contact_router

app = FastAPI(title="PenMan Writings API")

@app.get("/")
def health():
    return {"status": "PenMan backend running"}

# Include Routes
app.include_router(registration_router)
app.include_router(courses_router)
app.include_router(contact_router)

# Lambda handler
handler = Mangum(app)
