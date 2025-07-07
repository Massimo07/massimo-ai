from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.userService import UserService
from services.tokenService import TokenService
from models.token import Token
from utils.logger import logger

router = APIRouter(prefix="/api/v1/token", tags=["token"])

@router.post("/", response_model=Token)
async def login_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Ritorna JWT token per autenticazione.
    """
    user = await UserService.authenticate_user(form_data.username, form_data.password)
    if not user:
        logger.warning(f"Login fallito per {form_data.username}")
        raise HTTPException(status_code=401, detail="Credenziali non valide")
    access_token = TokenService.create_access_token(data={"sub": user.id, "role": user.role})
    logger.info(f"Login OK: {user.email}")
    return Token(access_token=access_token, token_type="bearer")
