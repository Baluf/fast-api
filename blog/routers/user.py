from fastapi import APIRouter, Depends, HTTPException
from .. import schemas, database, models

from sqlalchemy.orm import Session
from ..hashing import Hash
from . import outh2
router = APIRouter(prefix='/user', tags=['Users'])


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(outh2.get_current_user)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(outh2.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found")

    return user
