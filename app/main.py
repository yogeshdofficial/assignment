from fastapi import FastAPI
from app.routes import banks, branches

app = FastAPI(title="Bank Information API")


@app.get("/", tags=["Root"])
def index():
    """Health / status endpoint for the API."""
    return {"status": "ok", "service": "Bank Information API"}


app.include_router(banks.router)
app.include_router(branches.router)
