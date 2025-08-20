from fastapi import HTTPException, status, Request
import jwt
from .settings import settings
def get_current_user(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        return None
    token = auth.split(" ", 1)[1]
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc
