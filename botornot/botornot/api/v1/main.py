from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get("/", status_code=200)
def root():
    # redirect to docs
    return RedirectResponse(url="/docs")
