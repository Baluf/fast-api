from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from blog import schemas, database, models


from ..hashing import Hash
from ..jwt_token import create_access_token

router = APIRouter(prefix='/login', tags=['Authentication'])


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'incorrect password')

    access_token = create_access_token(
        data={"sub": user.email})

    return schemas.Token(access_token=access_token, token_type="bearer")
