from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "mayra@mayra.com":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Las credenciales son invalidas')
