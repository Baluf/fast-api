from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from blog import schemas, database, models

from ..hashing import Hash

router = APIRouter(prefix='/login', tags=['Authentication'])


@router.post('/')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'incorrect password')

    return user
