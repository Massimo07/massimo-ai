from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.user import User
from services.userService import UserService

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token/")

async def get_current_active_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception()
        user = await UserService.get_user_by_id(user_id)
        if not user:
            raise credentials_exception()
        return user
    except JWTError:
        raise credentials_exception()

def credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Non autorizzato",
        headers={"WWW-Authenticate": "Bearer"},
    )

def has_permission(user: User, role: str):
    # Puoi fare controllo avanzato dei ruoli qui
    if user.role != role:
        raise HTTPException(status_code=403, detail="Permesso negato")
