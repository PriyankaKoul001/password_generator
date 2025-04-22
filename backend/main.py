from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import random
import string

app = FastAPI()

# CORS for frontend to backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Can be refined
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate-password")
def generate_password(
    length: int = Query(..., ge=4),
    uppercase: int = Query(1, ge=0),
    lowercase: int = Query(1, ge=0),
    digits: int = Query(1, ge=0),
    special: int = Query(1, ge=0)
):
    total_required = uppercase + lowercase + digits + special
    if total_required > length:
        raise HTTPException(status_code=400, detail="Sum of character types exceeds password length")

    password_chars = []

    password_chars += random.choices(string.ascii_uppercase, k=uppercase)
    password_chars += random.choices(string.ascii_lowercase, k=lowercase)
    password_chars += random.choices(string.digits, k=digits)
    password_chars += random.choices(string.punctuation, k=special)

    remaining = length - len(password_chars)
    if remaining > 0:
        all_chars = string.ascii_letters + string.digits + string.punctuation
        password_chars += random.choices(all_chars, k=remaining)

    random.shuffle(password_chars)
    return {"password": ''.join(password_chars)}
