from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return [{"id": 1, "email": "user@example.com"}]
