from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Bank, BankBranchView

router = APIRouter(prefix="/banks", tags=["Banks"])


@router.get("/")
def get_banks(
    page: Optional[int] = Query(None, ge=1),
    page_size: Optional[int] = Query(None, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(Bank).order_by(Bank.name)

    if page is None or page_size is None:
        return query.all()

    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()

    return {"total": total, "page": page, "page_size": page_size, "items": items}


@router.get("/{bank_id}/branches")
def get_bank_branches(
    bank_id: int,
    page: Optional[int] = Query(None, ge=1),
    page_size: Optional[int] = Query(None, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = (
        db.query(BankBranchView)
        .filter(BankBranchView.bank_id == bank_id)
        .order_by(BankBranchView.branch)
    )

    if page is None or page_size is None:
        return query.all()

    total = query.count()
    offset = (page - 1) * page_size
    items = query.offset(offset).limit(page_size).all()

    return {"total": total, "page": page, "page_size": page_size, "items": items}
