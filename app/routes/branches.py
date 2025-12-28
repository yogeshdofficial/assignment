from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import BankBranchView

router = APIRouter(prefix="/branches", tags=["Branches"])


@router.get("/{ifsc}")
def get_branch(ifsc: str, db: Session = Depends(get_db)):
    """Return a single branch by IFSC code.

    Raises 404 when the branch is not found.
    """
    branch = db.query(BankBranchView).filter(BankBranchView.ifsc == ifsc).first()

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch
